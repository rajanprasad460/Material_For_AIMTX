from pathlib import Path
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else 'index.html')
text = path.read_text(encoding='utf-8')

if 'id="xor-gate"' in text:
    raise SystemExit('XOR section already exists; no changes made.')

css = r'''

    /* XOR lesson additions */
    .lesson-divider {
      margin: 72px 0 48px;
      padding: 32px;
      border-radius: var(--radius);
      background: linear-gradient(135deg, #102a67, #2457d6);
      color: #fff;
      box-shadow: var(--shadow);
    }
    .lesson-divider h2 { margin: 0 0 10px; }
    .lesson-divider p { margin: 0; color: #e7eeff; }
    .xor-network {
      width: 100%;
      min-height: 340px;
      display: block;
    }
    .xor-network line {
      stroke: var(--primary);
      stroke-width: 3;
      opacity: .72;
    }
    .xor-network circle {
      fill: #f7f9ff;
      stroke: var(--primary);
      stroke-width: 4;
    }
    .xor-network text {
      fill: var(--text);
      font-size: 24px;
      font-weight: 800;
      text-anchor: middle;
    }
    .xor-network .layer-label {
      fill: var(--muted);
      font-size: 18px;
      font-weight: 700;
    }
    .xor-parameter-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 14px;
    }
    .xor-trainer-controls {
      display: flex;
      gap: 14px;
      align-items: end;
      flex-wrap: wrap;
    }
    .xor-trainer-controls label {
      display: grid;
      gap: 6px;
      font-weight: 700;
    }
    .xor-trainer-controls input {
      width: 150px;
      padding: 10px 12px;
      border: 1px solid var(--border);
      border-radius: 10px;
      font: inherit;
    }
    .xor-trainer-controls button {
      border: 0;
      border-radius: 10px;
      padding: 11px 16px;
      background: var(--primary);
      color: #fff;
      font: inherit;
      font-weight: 800;
      cursor: pointer;
    }
    .xor-trainer-controls button.secondary { background: #667085; }
    .xor-predictions {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-top: 18px;
    }
    .xor-prediction {
      padding: 14px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: var(--surface-soft);
      text-align: center;
    }
    .xor-prediction strong {
      display: block;
      margin-top: 4px;
      color: var(--primary-dark);
      font-size: 1.25rem;
    }
    @media (max-width: 820px) {
      .xor-parameter-grid,
      .xor-predictions { grid-template-columns: 1fr; }
    }
'''

xor_html = r'''

    <div class="lesson-divider" id="xor-gate">
      <h2>Manual Training of an XOR Gate Neural Network</h2>
      <p>
        The XOR gate requires a hidden layer because its two output classes cannot be
        separated by a single straight decision boundary. We therefore use a 2–2–1
        sigmoid neural network.
      </p>
    </div>

    <section>
      <div class="section-title">
        <span class="section-number">X1</span>
        <h2>XOR-gate training data and network architecture</h2>
      </div>
      <div class="hero-grid">
        <div class="card">
          <h3>XOR-gate truth table</h3>
          <table class="truth-table" aria-label="XOR gate truth table">
            <thead>
              <tr><th>\(x_1\)</th><th>\(x_2\)</th><th>Desired output \(y_d\)</th></tr>
            </thead>
            <tbody>
              <tr><td>0</td><td>0</td><td>0</td></tr>
              <tr><td>0</td><td>1</td><td>1</td></tr>
              <tr><td>1</td><td>0</td><td>1</td></tr>
              <tr><td>1</td><td>1</td><td>0</td></tr>
            </tbody>
          </table>
        </div>
        <div class="card model-box">
          <div>
            <h3>2–2–1 neural network</h3>
            <div class="model-flow">
              <span class="node">2 inputs</span><span class="arrow">→</span>
              <span class="node">2 hidden neurons</span><span class="arrow">→</span>
              <span class="node">1 output</span>
            </div>
            \[\mathbf{x}\rightarrow(h_1,h_2)\rightarrow y\]
          </div>
        </div>
      </div>
      <div class="note" style="margin-top:18px;">
        A single sigmoid neuron can learn OR, but it cannot learn XOR because XOR is
        not linearly separable. The hidden layer creates nonlinear intermediate features.
      </div>
    </section>

    <section>
      <div class="section-title">
        <span class="section-number">X2</span>
        <h2>Hidden-layer model: visual explanation</h2>
      </div>
      <figure class="diagram-figure">
        <svg class="xor-network" viewBox="0 0 900 360" role="img" aria-label="Two input, two hidden neuron, one output neural network">
          <line x1="155" y1="105" x2="405" y2="105" />
          <line x1="155" y1="105" x2="405" y2="255" />
          <line x1="155" y1="255" x2="405" y2="105" />
          <line x1="155" y1="255" x2="405" y2="255" />
          <line x1="475" y1="105" x2="720" y2="180" />
          <line x1="475" y1="255" x2="720" y2="180" />
          <circle cx="120" cy="105" r="35" /><circle cx="120" cy="255" r="35" />
          <circle cx="440" cy="105" r="35" /><circle cx="440" cy="255" r="35" />
          <circle cx="755" cy="180" r="35" />
          <text x="120" y="113">x₁</text><text x="120" y="263">x₂</text>
          <text x="440" y="113">h₁</text><text x="440" y="263">h₂</text>
          <text x="755" y="188">y</text>
          <text class="layer-label" x="120" y="45">Input layer</text>
          <text class="layer-label" x="440" y="45">Hidden layer</text>
          <text class="layer-label" x="755" y="105">Output layer</text>
        </svg>
        <figcaption>Each input is connected to both hidden neurons, and both hidden neurons are connected to the output neuron.</figcaption>
      </figure>
    </section>

    <section>
      <div class="section-title">
        <span class="section-number">X3</span>
        <h2>Forward propagation through the hidden layer</h2>
      </div>
      <div class="grid-2">
        <div class="equation-card">
          <h3>Hidden neuron 1</h3>
          \[z_{h_1}=w_{11}x_1+w_{12}x_2+b_1\]
          \[h_1=\sigma(z_{h_1})\]
        </div>
        <div class="equation-card">
          <h3>Hidden neuron 2</h3>
          \[z_{h_2}=w_{21}x_1+w_{22}x_2+b_2\]
          \[h_2=\sigma(z_{h_2})\]
        </div>
      </div>
      <div class="equation-card highlight">
        <h3>Output neuron and loss</h3>
        \[z_o=v_1h_1+v_2h_2+b_o,\qquad y=\sigma(z_o)\]
        \[J=\frac{1}{2}(y_d-y)^2\]
      </div>
    </section>

    <section>
      <div class="section-title">
        <span class="section-number">X4</span>
        <h2>Backpropagation through the output and hidden layers</h2>
      </div>
      <div class="equation-card">
        <h3>Output-layer delta</h3>
        \[\boxed{\delta_o=(y-y_d)y(1-y)}\]
        \[\frac{\partial J}{\partial v_1}=\delta_oh_1,\quad
          \frac{\partial J}{\partial v_2}=\delta_oh_2,\quad
          \frac{\partial J}{\partial b_o}=\delta_o\]
      </div>
      <div class="grid-2">
        <div class="equation-card">
          <h3>Hidden neuron 1 delta</h3>
          \[\boxed{\delta_{h_1}=\delta_ov_1h_1(1-h_1)}\]
          \[\frac{\partial J}{\partial w_{11}}=\delta_{h_1}x_1,\quad
            \frac{\partial J}{\partial w_{12}}=\delta_{h_1}x_2\]
        </div>
        <div class="equation-card">
          <h3>Hidden neuron 2 delta</h3>
          \[\boxed{\delta_{h_2}=\delta_ov_2h_2(1-h_2)}\]
          \[\frac{\partial J}{\partial w_{21}}=\delta_{h_2}x_1,\quad
            \frac{\partial J}{\partial w_{22}}=\delta_{h_2}x_2\]
        </div>
      </div>
      <div class="note">
        During the backward pass, gradient information moves from the loss to the output
        neuron and then to both hidden neurons. The inputs themselves do not move backward.
      </div>
    </section>

    <section>
      <div class="section-title">
        <span class="section-number">X5</span>
        <h2>Gradient-descent update rules</h2>
      </div>
      <div class="equation-card">
        \[v_j^{\mathrm{new}}=v_j^{\mathrm{old}}-\eta\delta_oh_j,\qquad
          b_o^{\mathrm{new}}=b_o^{\mathrm{old}}-\eta\delta_o\]
        \[w_{ji}^{\mathrm{new}}=w_{ji}^{\mathrm{old}}-\eta\delta_{h_j}x_i,\qquad
          b_j^{\mathrm{new}}=b_j^{\mathrm{old}}-\eta\delta_{h_j}\]
      </div>
      <div class="xor-parameter-grid">
        <div class="result-box">Hidden neuron 1<strong>\(w_{11},w_{12},b_1\)</strong></div>
        <div class="result-box">Hidden neuron 2<strong>\(w_{21},w_{22},b_2\)</strong></div>
        <div class="result-box">Output neuron<strong>\(v_1,v_2,b_o\)</strong></div>
      </div>
      <p class="note" style="margin-top:18px;">
        The hidden neurons must not begin with identical parameters. Unequal initial values
        break symmetry and allow the neurons to learn different internal features.
      </p>
    </section>

    <section>
      <div class="section-title">
        <span class="section-number">X6</span>
        <h2>One complete XOR epoch: detailed calculation</h2>
      </div>
      <div class="equation-card highlight">
        <h3>Initial parameters</h3>
        \[w_{11}=0.10,\ w_{12}=0.20,\ b_1=0.30\]
        \[w_{21}=0.40,\ w_{22}=0.50,\ b_2=0.60\]
        \[v_1=0.70,\ v_2=0.80,\ b_o=0.90,\qquad \eta=0.5\]
        <p>Online gradient descent is used: after each sample, all relevant parameters are immediately updated.</p>
      </div>

      <details class="card" open>
        <summary><strong>Iteration 1: input \((0,0)\), target \(y_d=0\)</strong></summary>
        <h3 style="margin-top:18px;">1. Hidden-layer forward pass</h3>
        <div class="equation-card">
          \[z_{h_1}=0.10(0)+0.20(0)+0.30=0.3000\]
          \[h_1=\sigma(0.3000)=\frac{1}{1+e^{-0.3000}}=0.574443\]
          \[z_{h_2}=0.40(0)+0.50(0)+0.60=0.6000\]
          \[h_2=\sigma(0.6000)=0.645656\]
        </div>
        <h3>2. Output and loss</h3>
        <div class="equation-card">
          \[z_o=0.70(0.574443)+0.80(0.645656)+0.90=1.818635\]
          \[y=\sigma(1.818635)=0.860402\]
          \[J=\frac12(0-0.860402)^2=0.370146\]
        </div>
        <h3>3. Backpropagation</h3>
        <div class="equation-card">
          \[\delta_o=(0.860402-0)(0.860402)(1-0.860402)=0.103343\]
          \[\delta_{h_1}=0.103343(0.70)(0.574443)(1-0.574443)=0.017684\]
          \[\delta_{h_2}=0.103343(0.80)(0.645656)(1-0.645656)=0.018915\]
        </div>
        <h3>4. Parameter updates</h3>
        <div class="equation-card success">
          \[v_1'=0.70-0.5(0.103343)(0.574443)=0.670318\]
          \[v_2'=0.80-0.5(0.103343)(0.645656)=0.766638\]
          \[b_o'=0.90-0.5(0.103343)=0.848328\]
          <p>Because \(x_1=x_2=0\), all four input-to-hidden weight gradients are zero. Only the hidden biases change:</p>
          \[b_1'=0.30-0.5(0.017684)=0.291158,\qquad b_2'=0.60-0.5(0.018915)=0.590543\]
        </div>
      </details>

      <details class="card" style="margin-top:16px;">
        <summary><strong>Iteration 2: input \((0,1)\), target \(y_d=1\)</strong></summary>
        <p class="note" style="margin-top:18px;">This iteration starts with the parameters obtained after Iteration 1.</p>
        <div class="equation-card">
          \[z_{h_1}=0.10(0)+0.20(1)+0.291158=0.491158,\qquad h_1=0.620379\]
          \[z_{h_2}=0.40(0)+0.50(1)+0.590543=1.090543,\qquad h_2=0.748484\]
          \[z_o=0.670318(0.620379)+0.766638(0.748484)+0.848328=1.837996\]
          \[y=0.862711,\qquad J=\frac12(1-0.862711)^2=0.009424\]
        </div>
        <div class="equation-card">
          \[\delta_o=(0.862711-1)(0.862711)(1-0.862711)=-0.016261\]
          \[\delta_{h_1}=-0.016261(0.670318)(0.620379)(1-0.620379)=-0.002567\]
          \[\delta_{h_2}=-0.016261(0.766638)(0.748484)(1-0.748484)=-0.002347\]
        </div>
        <div class="equation-card success">
          \[v_1'=0.675362,\quad v_2'=0.772723,\quad b_o'=0.856459\]
          <p>Here \(x_1=0\), so \(w_{11}\) and \(w_{21}\) do not change. Since \(x_2=1\):</p>
          \[w_{12}'=0.20-0.5(-0.002567)=0.201283\]
          \[w_{22}'=0.50-0.5(-0.002347)=0.501173\]
          \[b_1'=0.292441,\qquad b_2'=0.591716\]
        </div>
      </details>

      <details class="card" style="margin-top:16px;">
        <summary><strong>Iteration 3: input \((1,0)\), target \(y_d=1\)</strong></summary>
        <div class="equation-card">
          \[z_{h_1}=0.10(1)+0.201283(0)+0.292441=0.392441,\qquad h_1=0.596870\]
          \[z_{h_2}=0.40(1)+0.501173(0)+0.591716=0.991716,\qquad h_2=0.729427\]
          \[z_o=0.675362(0.596870)+0.772723(0.729427)+0.856459=1.823207\]
          \[y=0.860950,\qquad J=0.009667\]
        </div>
        <div class="equation-card">
          \[\delta_o=-0.016646,\qquad \delta_{h_1}=-0.002705,\qquad \delta_{h_2}=-0.002539\]
        </div>
        <div class="equation-card success">
          \[v_1'=0.680329,\quad v_2'=0.778794,\quad b_o'=0.864782\]
          <p>Here \(x_2=0\), so \(w_{12}\) and \(w_{22}\) remain unchanged. Since \(x_1=1\):</p>
          \[w_{11}'=0.10-0.5(-0.002705)=0.101353\]
          \[w_{21}'=0.40-0.5(-0.002539)=0.401269\]
          \[b_1'=0.293794,\qquad b_2'=0.592985\]
        </div>
      </details>

      <details class="card" style="margin-top:16px;">
        <summary><strong>Iteration 4: input \((1,1)\), target \(y_d=0\)</strong></summary>
        <div class="equation-card">
          \[z_{h_1}=0.101353+0.201283+0.293794=0.596430,\qquad h_1=0.644839\]
          \[z_{h_2}=0.401269+0.501173+0.592985=1.495428,\qquad h_2=0.816892\]
          \[z_o=0.680329(0.644839)+0.778794(0.816892)+0.864782=1.939675\]
          \[y=0.874316,\qquad J=\frac12(0-0.874316)^2=0.382215\]
        </div>
        <div class="equation-card">
          \[\delta_o=0.096076,\qquad \delta_{h_1}=0.014970,\qquad \delta_{h_2}=0.011192\]
        </div>
        <div class="equation-card success">
          \[v_1'=0.649353,\quad v_2'=0.739553,\quad b_o'=0.816744\]
          \[w_{11}'=0.093868,\quad w_{12}'=0.193799,\quad b_1'=0.286309\]
          \[w_{21}'=0.395673,\quad w_{22}'=0.495577,\quad b_2'=0.587389\]
        </div>
      </details>

      <div class="card" style="overflow-x:auto; margin-top:20px;">
        <h3>One-epoch summary</h3>
        <table class="epoch-table">
          <thead>
            <tr><th>Iteration</th><th>Sample</th><th>Target</th><th>\(h_1\)</th><th>\(h_2\)</th><th>\(y\)</th><th>Loss</th><th>\(\delta_o\)</th></tr>
          </thead>
          <tbody>
            <tr><td>1</td><td>(0,0)</td><td>0</td><td>0.574443</td><td>0.645656</td><td>0.860402</td><td>0.370146</td><td>0.103343</td></tr>
            <tr><td>2</td><td>(0,1)</td><td>1</td><td>0.620379</td><td>0.748484</td><td>0.862711</td><td>0.009424</td><td>−0.016261</td></tr>
            <tr><td>3</td><td>(1,0)</td><td>1</td><td>0.596870</td><td>0.729427</td><td>0.860950</td><td>0.009667</td><td>−0.016646</td></tr>
            <tr><td>4</td><td>(1,1)</td><td>0</td><td>0.644839</td><td>0.816892</td><td>0.874316</td><td>0.382215</td><td>0.096076</td></tr>
          </tbody>
        </table>
      </div>
      <div class="equation-card success">
        \[\boxed{4\ \text{iterations}=1\ \text{epoch}}\]
        <p>The first epoch does not solve XOR. Repeating the same forward-pass, backpropagation, and update process gradually reduces the total loss.</p>
      </div>
    </section>

    <section>
      <div class="section-title">
        <span class="section-number">X7</span>
        <h2>Interactive XOR training</h2>
      </div>
      <div class="card">
        <p>Train the 2–2–1 network directly in the browser and inspect its four predictions.</p>
        <div class="xor-trainer-controls">
          <label>Epochs <input id="xorEpochs" type="number" min="1" max="100000" value="15000" /></label>
          <label>Learning rate <input id="xorLearningRate" type="number" min="0.01" max="2" step="0.01" value="0.5" /></label>
          <button id="xorTrainButton" type="button">Train XOR network</button>
          <button id="xorResetButton" class="secondary" type="button">Reset</button>
        </div>
        <p id="xorStatus" class="note" style="margin-top:18px;">Ready to train.</p>
        <div id="xorPredictions" class="xor-predictions"></div>
      </div>
    </section>
'''

js = r'''

    // Interactive XOR trainer (2 inputs, 2 hidden neurons, 1 output neuron)
    (() => {
      const sigmoid = z => 1 / (1 + Math.exp(-z));
      const data = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]];
      let p;

      function resetParameters() {
        p = {
          w11: 0.10, w12: 0.20, b1: 0.30,
          w21: 0.40, w22: 0.50, b2: 0.60,
          v1: 0.70, v2: 0.80, bo: 0.90
        };
      }

      function forward(x1, x2) {
        const h1 = sigmoid(p.w11*x1 + p.w12*x2 + p.b1);
        const h2 = sigmoid(p.w21*x1 + p.w22*x2 + p.b2);
        const y = sigmoid(p.v1*h1 + p.v2*h2 + p.bo);
        return {h1, h2, y};
      }

      function render(message) {
        const box = document.getElementById('xorPredictions');
        const status = document.getElementById('xorStatus');
        if (!box || !status) return;
        box.innerHTML = data.map(([x1,x2,target]) => {
          const y = forward(x1,x2).y;
          return `<div class="xor-prediction">(${x1}, ${x2}) → target ${target}<strong>${y.toFixed(4)}</strong></div>`;
        }).join('');
        status.textContent = message;
      }

      function train() {
        const epochs = Math.max(1, Number(document.getElementById('xorEpochs').value) || 15000);
        const eta = Math.max(0.0001, Number(document.getElementById('xorLearningRate').value) || 0.5);
        let finalLoss = 0;
        for (let epoch = 0; epoch < epochs; epoch++) {
          finalLoss = 0;
          for (const [x1,x2,target] of data) {
            const {h1,h2,y} = forward(x1,x2);
            finalLoss += 0.5 * (target-y) ** 2;
            const deltaO = (y-target) * y * (1-y);
            const deltaH1 = deltaO * p.v1 * h1 * (1-h1);
            const deltaH2 = deltaO * p.v2 * h2 * (1-h2);

            const oldV1 = p.v1;
            const oldV2 = p.v2;
            p.v1 -= eta * deltaO * h1;
            p.v2 -= eta * deltaO * h2;
            p.bo -= eta * deltaO;
            p.w11 -= eta * deltaH1 * x1;
            p.w12 -= eta * deltaH1 * x2;
            p.b1 -= eta * deltaH1;
            p.w21 -= eta * deltaH2 * x1;
            p.w22 -= eta * deltaH2 * x2;
            p.b2 -= eta * deltaH2;
          }
        }
        render(`Training complete: ${epochs.toLocaleString()} epochs, final epoch loss ${finalLoss.toFixed(6)}.`);
      }

      resetParameters();
      document.getElementById('xorTrainButton')?.addEventListener('click', train);
      document.getElementById('xorResetButton')?.addEventListener('click', () => {
        resetParameters();
        render('Parameters reset to the manual-example values.');
      });
      render('Ready to train.');
    })();
'''

if '</style>' not in text or '</main>' not in text or '</script>' not in text:
    raise SystemExit('Expected HTML markers were not found. The source page structure may have changed.')

text = text.replace('</style>', css + '\n  </style>', 1)
text = text.replace('<header class="hero">', '<header class="hero" id="or-gate">', 1)
text = text.replace(
    '<a href="https://aimtx.rajan-prasad.com.np/" aria-current="page">AI for Mechatronics</a>',
    '<a href="https://aimtx.rajan-prasad.com.np/" aria-current="page">AI for Mechatronics</a>\n        <a href="#or-gate">OR Gate</a>\n        <a href="#xor-gate">XOR Gate</a>',
    1
)
text = text.replace('  </main>', xor_html + '\n  </main>', 1)
last_script_close = text.rfind('  </script>')
if last_script_close == -1:
    raise SystemExit('Could not locate the final inline script.')
text = text[:last_script_close] + js + '\n' + text[last_script_close:]

backup = path.with_suffix(path.suffix + '.before-xor')
backup.write_text(path.read_text(encoding='utf-8'), encoding='utf-8')
path.write_text(text, encoding='utf-8')
print(f'Updated: {path}')
print(f'Backup:  {backup}')
