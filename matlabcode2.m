
%read the output variable from the file
output_variable = fileread('c_output.txt');

%Convert the string to a numeric array
%convert the numeric array to unsigned char
output_array = unit8(str2num(output_variable));

%resize to original size
resized_matrix = reshape(output_array, 256,256);

%display image
figure()
imshow(resized_matrix);
title('Black & White Image from C');