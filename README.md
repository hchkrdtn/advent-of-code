Solutions for Advent of Code [2018](https://adventofcode.com/2018), [2019](https://adventofcode.com/2019), [2020](https://adventofcode.com/2020), [2021](https://adventofcode.com/2021), [2022](https://adventofcode.com/2022), [2023](https://adventofcode.com/2023) and [2024](https://adventofcode.com/2024).

These solutions prioritize using [NumPy](http://cs231n.github.io/python-numpy-tutorial/) and speed above just about everything else. I am trying to be more **effective** and **efficient** in my programming.

MO

### Installation

1. Clone the code (https://github.com/hchkrdtn/advent-of-code.git) repository.
2. Install required packages. Currently `numpy` and `scipy`, packages for scientific computing, `pandas`, 
a package to manipulate data structures (tables) and data analysis, `pygame` and `matplotlib` packages 
for developing games and data visualization respectively. Please check `pygame` installation [instructions](https://www.pygame.org/wiki/GettingStarted).
3. I recommend using virtual environments, `conda` (preferred) or `virtualenv` for python 3.6+. 
for managing Python environments.  
In case of `conda`, the package management and deployment tool 
is called `miniconda` or `anaconda`. Create the environment from the terminal at the project 
folder (called `advent-of-code` here) and activate it:

   ```
   conda create -n advent-of-code python=3.7
   source activate advent-of-code
   ```
   or  
   ```
   virtualenv --python=python3.7 advent-of-code
   source venv/bin/activate
   ```
   
4. Install required packages individually if necessary. use `conda` again or  
you can also use `pip` for installing packages:

   ```
   conda install numpy
   conda install scipy
   conda install pandas
   conda install -c conda-forge matplotlib
   pip install pygame
   ```
   or
    ```
   pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
   pip install pygame
   ```

### Running

Run from advent-of-code folder (master branch) or switch to other branches: 

`git branch -a git checkout master`
