Here you can find the code to reproduce experiments in the submission.

To be able to run the experiments, you need to perform the following steps:
1. Download `adult.zip` file from https://www.kaggle.com/datasets/uciml/adult-census-income.
2. Unzip the archive and place extracted `adult.csv` in folder `datasets/census`.
3. Create a python 3 environment and install all the requirements there with ```pip install -r requirements.txt```.
4. Run train_census.py: ```python train_census.py```.
5. Run perform_atacks.py: ```python perform_attacks.py```.
6. Run plot_shapley.py: ```python plot_shapley.py```.
This script will create plots with Shapley values of the original and the manipulated models with both mean and median subset functions.
The plots can be found in `census/res_<attack number>/images`.
7. Run plot_lipschitz_bound.py: ```python plot_lipschitz_bound.py```.
This script will plot the Lipschitz constant. The plot can be found in project root.
