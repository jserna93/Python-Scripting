

%read pgm image
img = imread('mickey1.png');

%specify the target size
%targetSize = [256, 256];

%resize image
%img = imresize(img, targetSize);

%reshape the image into a 1D array
img_1d = reshape(img, 1, []);

%write the data to a file
dlmwrite('input.txt', img_1d, 'delimiter', ' ');