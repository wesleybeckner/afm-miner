alignImage(static, moving, level_iters):
    """The Symmetric Normalization algorithm uses a multi-resolution approach by building a Gaussian Pyramid.
    The static image is used a reference; a transformation that transforms the moving image into the
    static image is found and applied to the static image.  Returns overlay images, error image, and transformation matrix. 
    Uses CrossCorrelation metric which makes sense for aligning AFM topography. 
    
    INPUT: static and moving are both 2d arrays of the same dimension.
    Level_iters is a list (typically 4 entries) defines
    the number of iterations a user wants at each level of the pyramid, with the 0th entry referring to the 
    finest resolution.
    
    OUTPUT: overlayimages: an image with the static, moving, and overlay images
            errorimage: the difference between the warped_moving image and the static reference. THe flatter 
            the better.
            transformmatrix: the matrix corresponding to the forward transformation of a matrix."""
    
    from dipy.align.imwarp import SymmetricDiffeomorphicRegistration
    from dipy.align.metrics import SSDMetric, CCMetric, EMMetric
    from dipy.viz import regtools

    dim = static.ndim
    metric = CCMetric(dim)
    sdr = SymmetricDiffeomorphicRegistration(metric, level_iters, inv_iter = 50)
    mapping = sdr.optimize(static, moving)
    warped_moving = mapping.transform(moving, 'linear')
    overlayimages = regtools.overlay_images(static, warped_moving, 'Static','Overlay','Warped moving',
   'direct_warp_result.png')
    errorimage = plt.matshow(warped_moving-static, cmap='viridis')
    transformmatrix=mapping.forward
    
    
    return overlayimages, errorimage, transformmatrix
