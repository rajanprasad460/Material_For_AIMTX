# AI for Mechatronics — Interactive Course Portal

Website: https://aimtx.rajan-prasad.com.np/

An interactive postgraduate teaching portal with mathematical walkthroughs, numerical examples, interactive demonstrations, lecture slides, quizzes, and Google Colab exercises.

## Course outline

The homepage uses six collapsible lessons. The course navigation and sidebar open the selected unit.

| Unit | Topic | Main content |
| --- | --- | --- |
| 01 | Artificial Neural Networks | Single-neuron OR gate, forward propagation and manual backpropagation |
| 02 | Multilayer Neural Networks | XOR gate, hidden layers and interactive training |
| 03 | Convolutional Neural Networks | CNN fundamentals, convolution, activation, padding and pooling |
| 04 | Transfer Learning | VGG16 bearing-defect classification and evaluation |
| 05 | Recurrent Neural Networks | Sequence memory, recurrent states and training |
| 06 | Fuzzy Logic & ANFIS | Gaussian membership functions, first-order Sugeno rules, least-squares consequent estimation and interactive inference |

ANFIS appears immediately after Unit 05 in the main course lesson stream, before the independent Colab notebook library.

## Other course resources

- Quiz access and instructions.
- Lecture slide PDFs and syllabus.
- Colab notebook library for classroom demonstrations.
- Responsive heading navigation, unit navigation, and course outline sidebar.

## Repository files

- `index.html`: main page, all six lessons, styles, mathematical equations, and interactive JavaScript.
- `assets/`: lecture PDFs, Colab notebooks, illustrations, and supporting media.
- `CNAME`: custom domain configuration.
- `.htaccess`: optional hosting configuration.
- `homepage-module-snippet.html`: optional link card for the instructor's main website.
- `add_xor_to_page.py` and `index.html.before-xor`: historical development artifacts, not the current homepage.

## Deployment and verification

Deploy the root `index.html` with the `assets/` directory, preserving relative paths. The live address is https://aimtx.rajan-prasad.com.np/.

After deployment, verify the lesson order (01–06), expand/collapse navigation, OR/XOR training controls, CNN illustrations, ANFIS plot and slider, lecture resource links, and mobile layout.

Direct ANFIS link: https://aimtx.rajan-prasad.com.np/#anfis-interactive

## Implementation notes

The website is static HTML, CSS, and JavaScript. MathJax is loaded from a CDN for equation typesetting. The ANFIS numerical example fixes two Gaussian premise functions and calculates the four first-order Sugeno consequent coefficients using least squares; it does not train premise parameters in the browser.

## Instructor

For the instructor's current professional profile and contact information, visit **https://rajan-prasad.com.np/**. Contact details are intentionally not duplicated in this repository.
