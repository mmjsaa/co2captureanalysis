# Adsorption Kinetics Modelling
Adsorption kinetic models are essential tools for understanding the dynamic processes by which adsorption occurs over time. These models aim to characterise and predict the rate at which adsorption equilibrium is reached between the adsorbate and adsorbent. Three of the most common used for adsorption studies are the Avrami kinetic model, the Pseudo First Order kinetic model, and the Pseudo Second Order kinetic model, which are the three kinetic models I chose to use. These equations are also discussed extensively in [literature](https://link.springer.com/chapter/10.1007/978-3-319-18875-1_3). The Avrami kinetic model, commonly applied to describe solid-state reactions, has found utility in adsorption kinetics by expressing the fractional surface coverage as a function of time. The Pseudo First Order kinetic model assumes a linear relationship between the logarithm of the remaining adsorption capacity and time, providing insights into the initial adsorption stages. On the other hand, the Pseudo second Order kinetic model, which assumes chemisorption as the rate-limiting step, often offers superior accuracy in predicting adsorption kinetics. However, in the context of this study, the Pseudo-Second Order kinetc model was actually the least accurate, partly due to the porosity of the activated carbon. These models aid in interpreting experimental data, determining the controlling mechanisms of adsorption processes, and optimising conditions for various applications, such as environmental remediation and separation technologies. In these equations, $t$ refers to the time, $qe$ refers to the uptake of $\ce{CO2}$, and the other variables are parameters which define each equation.

## Avrami Kinetic Model
$$qe \cdot (1 - \exp(-kA \cdot t^{nA}))$$

## Pseudo First Order Kinetic Model
$$qe \cdot (1 - \exp(-kf \cdot t))$$

## Pseudo Second Order Kinetic Model
$$\frac{ks \cdot t \cdot qe^2}{1 + qe \cdot ks \cdot t}$$
