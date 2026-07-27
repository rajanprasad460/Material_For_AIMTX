# AI for Mechatronics subdomain package

Recommended public address:

    https://aimtx.rajan-prasad.com.np/

## Package contents

- `index.html` — complete interactive OR-gate lesson
- `assets/single_neuron_and_backpropagation.png`
- `assets/forward_and_backpropagation_overview.png`
- `OR_Gate_Manual_Backpropagation.ipynb`
- `homepage-module-snippet.html` — optional card for the main homepage
- `.htaccess` — optional Apache directory settings

## Recommended deployment

1. In your domain or hosting control panel, create the subdomain:

       aimtx.rajan-prasad.com.np

2. Point the subdomain to a dedicated document root, for example:

       public_html/aimtx/

   Some hosts create a separate folder automatically, such as:

       aimtx.rajan-prasad.com.np/

3. Upload the CONTENTS of this package into that document root. The final structure
   should look like:

       document-root/
       ├── index.html
       ├── OR_Gate_Manual_Backpropagation.ipynb
       ├── .htaccess
       └── assets/
           ├── single_neuron_and_backpropagation.png
           └── forward_and_backpropagation_overview.png

4. Enable SSL/HTTPS for the subdomain.

5. Confirm that this address opens:

       https://aimtx.rajan-prasad.com.np/

## DNS choices

Use whichever option your hosting provider recommends:

- `A` record: point `aimtx` to the hosting server's IP address.
- `CNAME` record: point `aimtx` to the hostname supplied by the hosting platform.

Do not write the URL as `aimtx.https://rajan-prasad.com.np/`.
The correct format is:

    https://aimtx.rajan-prasad.com.np/

## Main-site module

Copy `homepage-module-snippet.html` into the main website homepage where you want
the teaching-resource card to appear. It already links to the subdomain.

## Notebook link

The page downloads the notebook from the same subdomain:

    https://aimtx.rajan-prasad.com.np/OR_Gate_Manual_Backpropagation.ipynb

## Optional direct Google Colab link

After placing the notebook in a public GitHub repository, use:

    https://colab.research.google.com/github/USERNAME/REPOSITORY/blob/main/OR_Gate_Manual_Backpropagation.ipynb

MathJax is loaded from a CDN, so internet access is required for equation rendering.
