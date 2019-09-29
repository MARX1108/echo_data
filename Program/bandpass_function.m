function bandpass_function(FileName,DataPathWay,FigPathWay)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
%% Check Data
cd_name=[DataPathWay];
cd(cd_name) 
data_mat = load(FileName);
fs=400e3;% we are using 400e3;
f = data_mat;
t0= 0;  % Select the start time t0, time duration you want to do the bandpass
t1= 1;  % Select the end time t1
t=t0:1/fs:t1;
inp=f;Alltime_start=[];Alltime_end=[];
%% FIR Bandpass filter Parameters
FilPara.Fstop1 = 19e3;      % First Stopband Frequency
FilPara.Fpass1 = 21e3;      % First Passband Frequency
FilPara.Fpass2 = 45e3;      % Second Passband Frequency
FilPara.Fstop2 = 50e3;      % Second Stopband Frequency
FilPara.Astop1 = 60;        % First Stopband Attenuation (dB)
FilPara.Apass = 0.5;        % Passband Ripple (dB)
FilPara.Astop2 = 60;        % Second Stopband Attenuation (dB)                            % fs: sampling frequency
%% make the bandpass filter 
h = fdesign.bandpass(FilPara.Fstop1, FilPara.Fpass1, FilPara.Fpass2, FilPara.Fstop2, FilPara.Astop1, FilPara.Apass, FilPara.Astop2, fs);
Hd = design(h, 'equiripple');
fil=Hd.Numerator;
%% save the filter
name=['Band_fil_' num2str(fs) '_' num2str(FilPara.Fpass1) '_' num2str(FilPara.Fpass2) '.wav'];
save(name,'fil','fs','FilPara');
%% Filter Process
out=filtfilt(fil,1,inp);
%save('out','out','fs');% Save the filtered data

%% Plot
f = figure('visible', 'off');
spectrogram(out(:,1),hanning(256),128,256,fs,'yaxis');
 [~,ps] = spectrogram(out(:,1),[],[],[],fs,'yaxis');
 mtrix=spectrogram(out(:,1),hanning(256),128,256,fs,'yaxis');

colorbar('off'); 
 
% title('')
% xlabel('')
% ylabel('')
% set(gca,'xticklabel',{[]})
% set(gca,'yticklabel',{[]})

ylim ([15 55])

NewFileName=erase(FileName,".txt"); 
FigName=strcat(NewFileName,'.jpg'); 
saveas(gcf, fullfile(FigPathWay, FigName), 'jpeg');

close(f)

end

