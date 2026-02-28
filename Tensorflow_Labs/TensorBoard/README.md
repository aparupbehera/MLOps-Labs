# Weight Histograms & Gradient Tracking — CIFAR-10 with PyTorch + TensorBoard


---

## Exercise

Training the same CNN architecture twice on CIFAR-10, with one difference:

| Run | Setup |
|-----|-------|
| `run_no_bn` | CNN **without** Batch Normalization |
| `run_with_bn` | CNN **with** Batch Normalization |

By comparing two runs side-by-side in TensorBoard, the effect of batch normalisation becomes visible 

---

## CIFAR-10

CIFAR-10 is a dataset of 60,000 colour images (32×32 pixels) split across 10 classes:

> airplane · automobile · bird · cat · deer · dog · frog · horse · ship · truck

---

## TensorBoard Components

### Scalars
TensorBoard is plotting training loss, validation loss, training accuracy, validation accuracy, and learning rate. Also plotting gradient norms here (one line per layer), which is the key thing that makes this exercise different from a standard training notebook.

### Histograms
TensorBoard is displaying the full distribution of each layer's weights as a histogram that evolves over time. A layer that is learning will show its distribution gradually spreading out and shifting. A layer that is stagnating will show a flat, narrow distribution staying near zero.

### Expectation
- In `run_no_bn`: earlier conv layers are receiving weaker gradient signals than later layers — the histograms for `conv1` are moving less than those for `conv3`
- In `run_with_bn`: gradient norms are staying more consistent across all layers — batch normalisation is smoothing out the gradient flow

---

## How to Run It

**1. Install dependencies:**
```bash
pip install -r requirements.txt
```

**2. Launch Jupyter:**
```bash
jupyter notebook cifar10_tensorboard.ipynb
```

**3. Run all cells top to bottom.**

**4. Launch TensorBoard:**
The notebook is launching TensorBoard inline via `%tensorboard --logdir runs`.
If it does not appear, open a terminal and run:
```bash
tensorboard --logdir runs
```
Then open **http://localhost:6006** in any browser.

---

