%% House keeping

clc
clear 

%% main script
disp('first select where the data is');
disp('then select where you want to store is');

[DataPathWay] = ...
    uigetdir('C:\Users\77465\OneDrive - Virginia Tech\Desktop\Code\Python\echo_data'); 
[FigPathWay] = ...
    uigetdir('C:\Users\77465\OneDrive - Virginia Tech\Desktop\Code\Python\echo_data'); 

cd ([DataPathWay])

data_folder=dir('*.txt'); 
number_of_files=size(data_folder,1); 

for i=1:number_of_files % the number of files you want to process 
    FileName=data_folder(i).name; 
    bandpass_function(FileName,DataPathWay,FigPathWay); 
end 


