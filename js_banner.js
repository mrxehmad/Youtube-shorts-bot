const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');

const videosDir = './vids';
const outputDir = './out';
const topText = 'Subscribe <3';
const bottomText = 'Sweatwise @2023';

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

const videos = fs.readdirSync(videosDir).filter(file => path.extname(file) === '.mp4');

videos.forEach((videoFile, index) => {
  const inputPath = path.join(videosDir, videoFile);
  const outputPath = path.join(outputDir, `output_${index}.mp4`);

  const ffmpeg = spawn('ffmpeg', [
    '-i', inputPath,
    '-vf', `drawtext=fontfile=Arial.ttf:text='${topText}':x=(w-tw)/2:y=40:fontsize=64:fontcolor=white:box=1:boxcolor=black@0.5:boxborderw=10, drawtext=fontfile=Arial.ttf:text='${bottomText}':x=(w-tw)/2:y=h-th-40:fontsize=64:fontcolor=white:box=1:boxcolor=black@0.5:boxborderw=10`,
    '-codec:a', 'copy',
    '-codec:v', 'libx264',
    '-crf', '18',
    '-preset', 'fast',
    '-y',
    outputPath
  ]);

  ffmpeg.stderr.on('data', (data) => {
    console.error(`FFmpeg stderr: ${data}`);
  });

  ffmpeg.on('close', (code) => {
    console.log(`FFmpeg exited with code ${code}`);
  });
});