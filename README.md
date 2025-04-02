# Quantization Index Modulation (QIM) Steganography Tool

This Python implementation demonstrates how to hide secret messages in images using Quantization Index Modulation, a robust digital watermarking technique.

## Features

- Embeds text messages into PNG images using QIM algorithm
- Extracts hidden messages from encoded images
- Calculates PSNR (Peak Signal-to-Noise Ratio) to measure embedding quality
- Supports multi-line text messages
- Preserves original image dimensions

## Requirements

- Python 3.x
- Required packages:
  - NumPy
  - Pillow (PIL)
  - Math (standard library)
  - OS (standard library)

## Installation

```bash
pip install numpy pillow
```

## Usage

1. Place your source image (`image.png`) in the same directory
2. Run the script:
   ```bash
   qim.py
   ```
3. Follow the prompts:
   - Enter your secret message (press Enter twice to finish)
   - Specify the quantization step (q) - typically between 2-10
4. The modified image will be saved as `result.png`

To extract a message:
1. Run the script again with an encoded image
2. Provide the same quantization step (q) used during embedding
3. View the extracted message in the console

## Technical Details

### Embedding Process:
1. Converts message to binary representation
2. Quantizes image pixels based on the specified step (q)
3. Embeds each bit by modifying pixel values in the LSB
4. Calculates and displays PSNR metric

### Extraction Process:
1. Analyzes pixel quantization patterns
2. Reconstructs the binary message
3. Converts back to text format

## Parameters

- **Quantization Step (q)**: Controls the trade-off between:
  - Visibility (higher q = more noticeable changes)
  - Robustness (higher q = more resistant to compression/noise)
  - Capacity (higher q = fewer bits can be embedded)

Typical values range from 2-10 depending on application requirements.

## Output

- Saves multiple versions of the encoded image (`res_0.png`, `res_1.png`, etc.)
- Displays PSNR value (higher is better, >30dB generally acceptable)
- Shows extracted message in console

## Limitations

- Works best with lossless formats (PNG)
- Message capacity limited by image dimensions
- Not resistant to aggressive compression or scaling
