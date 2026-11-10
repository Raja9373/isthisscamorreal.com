import { Jimp } from 'jimp';

async function convert() {
  try {
    const image = await Jimp.read('public/assets/aistudio/image_e3141eaa.png');
    await image.write('public/og-image.jpg', { quality: 80 });
    console.log('Successfully converted compressed public/og-image.jpg');
  } catch (err) {
    console.error('Error converting image:', err);
  }
}

convert();
