# Crack-Detection
Detection of cracks using deep-learning and image processing techniques on car parts

## Image Processing ##
Initially, some filteration techniques are used to process the raw images so that they can be further used in the deep learning model.

### Log-transformation ###
Logarithmic transformation of an image is one of the gray level image transformations. Log transformation of an image means replacing all pixel values, present in the image, with its logarithmic values. Log transformation is used for image enhancement as it expands dark pixels of the image as compared to higher pixel values. 

### Bilateral filtering ###
Bilateral filtering also takes a Gaussian filter in space, but additionally considers one more Gaussian filter which is a function of pixel difference. The Gaussian function of space makes sure that only nearby pixels are considered for blurring, while the Gaussian function of intensity difference makes sure that only those pixels with similar intensities to the central pixel are considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.
* d: Diameter of each pixel neighborhood.
* sigmaColor: Value of sigma  in the color space. The greater the value, the colors farther to each other will start to get mixed.
* sigmaSpace: Value of sigma  in the coordinate space. The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.

### Morphological filtering ###
Morphological transformations are some simple operations based on the image shape. It is normally performed on binary images. It needs two inputs, one is our original image, second one is called structuring element or kernel which decides the nature of operation.
* Erosion -  A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
* Dilation - It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it.
* Opening - Opening is just another name of erosion followed by dilation. It is useful in removing noise.
* Closing - Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.

