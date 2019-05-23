GraRep
============================================
A SciPy implementation of "GraRep: Learning Graph Representations with Global Structural Information" (WWW 2015).
<p align="center">
  <img width="800" src="grarep.png">
</p>
<p align="justify">
In this paper, we present GraRep, a novel model for learning vertex representations of weighted graphs. This model learns low dimensional vectors to represent vertices appearing in a graph and, unlike existing work, integrates global structural information of the graph into the learning process. We also formally analyze the connections between our work and several previous research efforts, including the DeepWalk model of Perozzi et al. as well as the skip-gram model with negative sampling of Mikolov et al. We conduct experiments on a language network, a social network as well as a citation network and show that our learned global representations can be effectively used as features in tasks such as clustering, classification and visualization. Empirical results demonstrate that our representation significantly outperforms other state-of-the-art methods in such tasks.</p>


This repository provides a SciPy implementation of GraRep as described in the paper:

> GraRep: Learning Graph Representations with Global Structural Information.
> ShaoSheng Cao, Wei Lu, and Qiongkai Xu.
> WWW, 2015.
> [[Paper]](https://www.researchgate.net/profile/Qiongkai_Xu/publication/301417811_GraRep/links/5847ecdb08ae8e63e633b5f2/GraRep.pdf)

### Requirements
The codebase is implemented in Python 3.5.2. package versions used for development are just below.
```
networkx          1.11
tqdm              4.28.1
numpy             1.15.4
pandas            0.23.4
texttable         1.5.0
scipy             1.1.0
argparse          1.1.0
```
### Datasets
The code takes graphs for training from an input folder where each graph is stored as a JSON. Graphs used for testing are also stored as JSON files. Every node id and node label has to be indexed from 0. Keys of dictionaries are stored strings in order to make JSON serialization possible.

Every JSON file has the following key-value structure:

```javascript
{"edges": [[0, 1],[1, 2],[2, 3],[3, 4]],
 "labels": {"0": "A", "1": "B", "2": "C", "3": "A", "4": "B"},
 "target": 1}
```
The **edges** key has an edge list value which descibes the connectivity structure. The **labels** key has labels for each node which are stored as a dictionary -- within this nested dictionary labels are values, node identifiers are keys. The **target** key has an integer value which is the class membership.

### Outputs

The predictions are saved in the `output/` directory. Each embedding has a header and a column with the graph identifiers. Finally, the predictions are sorted by the identifier column.

### Options
Training a CapsGNN model is handled by the `src/main.py` script which provides the following command line arguments.

#### Input and output options
```
  --training-graphs   STR    Training graphs folder.      Default is `dataset/train/`.
  --testing-graphs    STR    Testing graphs folder.       Default is `dataset/test/`.
  --prediction-path   STR    Output predictions file.     Default is `output/watts_predictions.csv`.
```
#### Model options
```
  --epochs                      INT     Number of epochs.                  Default is 100.
  --batch-size                  INT     Number fo graphs per batch.        Default is 32.
  --gcn-filters                 INT     Number of filters in GCNs.         Default is 20.
  --gcn-layers                  INT     Number of GCNs chained together.   Default is 2.
  --inner-attention-dimension   INT     Number of neurons in attention.    Default is 20.  
  --capsule-dimensions          INT     Number of capsule neurons.         Default is 8.
  --number-of-capsules          INT     Number of capsules in layer.       Default is 8.
  --weight-decay                FLOAT   Weight decay of Adam.              Defatuls is 10^-6.
  --lambd                       FLOAT   Regularization parameter.          Default is 0.5.
  --theta                       FLOAT   Reconstruction loss weight.        Default is 0.1.
  --learning-rate               FLOAT   Adam learning rate.                Default is 0.01.
```
### Examples
The following commands learn a model and save the predictions. Training a model on the default dataset:
```
python src/main.py
```
<p align="center">
  <img width="500" src="capsgnn.gif">
</p>

Training a CapsGNNN model for a 100 epochs.
```
python src/main.py --epochs 100
```
Changing the batch size.
```
python src/main.py --batch-size 128
```
