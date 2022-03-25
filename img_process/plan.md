# Image Processing Subsystem

## Purpose
Take Video frames and turn them into barcode hashes

## Overall Process

1. Load the frame from file
2. Superimpose a grid of test points aligned with the hexagonal pattern of triangles in the image
	a. This will be a manual process
	b. Automated processes possible!
3. Check the color at each grid point. 
	a. if "dark", report as zero. 
	b. if "light", report as one. 
4. Encode the result portably
	a. First thought is as 4 32-bit hex values (i.e. 0x3A0CFF23)
	b. Alternatively, store each column of triangles separately for easier chunking. (E.G. E, 10, 19, 7F, 23) 

## Tasks

1. Create a function that gives coordinates for a half-hexagonal grid. 
