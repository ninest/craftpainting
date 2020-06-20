<h1 align="center">Craftpainting</h1>
<p align="center">Create Minecraft-like paintings in the terminal</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-Python-black?style=flat-square&" alt="Made with Python" />
  <a href="http://makeapullrequest.com/"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="Make a PR" /></a>
  <img src="https://img.shields.io/github/license/ninest/craftpainting?style=flat-square" alt="MIT" />
  <a href="https://www.buymeacoffee.com/ninest">
    <img src="https://img.shields.io/badge/Donate-Buy%20Me%20A%20Coffee-orange.svg?style=flat-square" alt="Buy Me A Coffee">
  </a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/painting_sunset_dense.jpg" alt="sunset dense" width="500">
</p>


## 🚀 Usage

```bash
craftpainting input_path.png -s SIZE -r REPETITIONS -o output_path.png 
```

### size
Enter a string of `WxH`, such as `2x1`. Units are Minecraft blocks, so a width of `2x1` translates to an image of `32x16`.

### repetitions
The number of times enlarge the image. By default, an image `32x16` or `48x32` is too small and doesn't look good.

The value of `-r` dictates how many times each pixel should be multiplied. It's `15` by default, so an image of size `2x1` in blocks looks like it's `32x16` pixels, but is actually `480x240`.

Set to `0` to get the minimum possible size.

### gray
Append `-g` (or `--gray`) to the command to make the painting black and white.

### outputpath
If no output path is specified, the image will be shown, but won't be saved.

## 🏳️‍🌈 Examples
### Sunset dense
```bash
craftpainting sunset_dense.jpg -o painting_sunset_dense.jpg
```
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/painting_sunset_dense.jpg" alt="sunset dense" width="300">
</p>

#### Original
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/sunset_dense.jpg" alt="sunset dense" width="300">
</p>

### Beach
```bash
craftpainting beach.png -s 3x2 -o painting_beach.png
```
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/painting_beach.png" alt="beach" width="300">
</p>

#### Original
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/beach.png" alt="beach" width="300">
</p>

### code
```bash
craftpainting code.jpg -s 2x2 -o painting_code.jpg
```
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/painting_code.jpg" alt="code" width="300">
</p>

#### Original
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/code.jpg" alt="code" width="300">
</p>


### Landscape
```bash
craftpainting landscape.jpg -g -r 5 -o painting_landscape.jpg
```

Smaller values of `repetitions` produce images of smaller sizes.
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/painting_landscape.jpg" alt="code" width="300">
</p>

#### Original
<p align="center">
  <img src="https://raw.githubusercontent.com/ninest/craftpainting/master/images/landscape.jpg" alt="code" width="300">
</p>


## 🛠 Build setup

```bash
cd src/
pipenv shell
pipenv install
```

<!-- ## 😱 Issues and limitations -->

## 📜 License
- MIT
- Sunset Dense taken from [Minecraft Gamepedia](https://minecraft.gamepedia.com/Painting)
- Some images taken from [Pexels](https://www.pexels.com/)

<!-- ## 🔖 Legal attribution -->
<!-- Google Play and the Google Play logo are trademarks of Google LLC. -->