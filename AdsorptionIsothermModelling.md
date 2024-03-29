# Adsorption Isotherm Models
Adsorption isotherm models are mathematical representations that describe the relationship between the amount of adsorbate molecules adsorbed onto a surface and the concentration or partial pressure of the adsorbate in the surrounding fluid. These models play a crucial role in understanding and predicting adsorption behavior, guiding the design and optimisation of various processes, such as gas separation, wastewater treatment, and catalysis. In this context, they are being used to describe the $\ce{CO2}$ adsorption ability of an adsorbent to be used in power plants. Commonly used adsorption isotherm models include the Langmuir, Freundlich, Sips, and Toth models, which are also the four models I used for my analysis.

More information on the specifics of these models can be found in several research papers, such as [here](), however, to briefly summarise each model; the Langmuir adsorption isotherm assumes monolayer adsorption onto a homogeneous surface, the Freundlich adsorption isotherm represents multilayer adsorption on heterogeneous surfaces, the Sips adsorption isotherm combines features of both Langmuir and Freundlich, and the Toth adsorption isotherm accounts for interactions beyond monolayer coverage. Based on this, and due to the nature of the context of my study, Sips and Toth are found to be far superior in accuracy when compared to Freundlich and Langmuir. In these equations, $P$ refers to the partial partial, $q_{e}$ refers to the amount of $\ce{CO2}$ adsorbed, and the other variables are parameters which define each equation.

## Freundlich
$$q_e = K_{F} P^{\frac{1}{n}}$$

## Langmuir
$$q_e = \frac{q_{\text{max}} \cdot b \cdot P}{{1 + b \cdot P}}$$

## Sips
$$q_e = \frac{q_{\text{max}} \cdot (b \cdot P)^{\frac{1}{n}}}{{1 + (b \cdot P)^{\frac{1}{n}}}}$$

## Toth
$$q_e = \frac{q_{\text{max}} \cdot b \cdot P}{{(1 + (b \cdot P)^{n})^{\frac{1}{n}}}}$$

---
# Results of Adsorption Isotherms
The results using the sample data and Python code are shown below:

![isothermresults](https://github.com/mmjsaa/co2captureanalysis/blob/9a2c2e2d5ba9c3b652b851b03804d383f7630fe4/Attachments/AdsorptionIsothermModelResult.svg)

| Model | Maximum Amount Adsorbed | Constant | Heterogeneity Parameter | Affinity Constant |
|---|---|---|---|---|
| Freundlich | - | 1.269478747861734 | 2.5068212939675436 | - |
| Langmuir | 9.34126991003779 | - | - | 0.04210289607846775 | 
| Sips | 11.74056043630181 | - |1.334842243798242 | 0.02356151583989827 |
| Toth | 13.936173113857384 | - |0.535858948991538 | 0.06291766711898603 |

