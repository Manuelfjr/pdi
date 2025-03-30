# Atividade 01

* **Aluno:** Manuel Ferreira Junior
* **Disciplina:** Processamento Digital de Imagens

# Questão 01

**Considere a imagem do cameraman na atividade (120x120 pixels).**

**A fotografia (física) original foi digitalizada com 75 dpi, gerando uma imagem com 120 x 120 pixels. Após a digitalização, o usuário achou que a imagem ficou pequena e decidiu ampliá-la para o dobro do tamanho (240x240 pixels). Disserte sobre o que haverá de semelhanças e diferenças entre essa imagem ampliada e uma imagem gerada por um novo processo de digitalização feito a 150 dpi.**

**R.:**

* **Semelhanças**:
  
  * **Mesma imagem**: apesar dos processos de digitalização serem diferentes (um a 75 dpi e outro a 150 dpi), a imagem devera representar o mesmo cenário.
  
  * **Dimensões**: as dimensões devem se conservar.
  
* **Diferenças**:
  
  * **Qualidade**: Qualidade da iamgem pode ser reduzida drasticamente quando comparamos uma imagem de 75 dpi com uma de 150 dpi.

  * **Nitidez**: A imagem com 150 dpi deve apresentar uma riqueza maior de detalhes na imagem quando comparada a 

  * **Tamanho**: O tamanho do arquivo pode aumentar significativamente para a imagem de 150 dpi;


# Questão 02
**Disserte sobre a relação entre amostragem e quantização e o espaço necessário para armazenamento de uma imagem**


# Questão 03

**Sabendo que o modelo CMYK é usado em dispositivos de impressão e que 
cada valor de Ciano (C), Magenta (M), Amarelo (Y) e Preto (K) correspondem a 
uma quantidade de tinta a ser usada na mistura para impressão, gerando 
diferentes cores. Considerando a conversão de RGB para CMYK apresentada no 
slide 18 da aula de Modelos de Cores, que problema poderíamos ter se o cálculo 
da componente K fosse dado como abaixo?** 

<p align="center">
<strong>K = 1 - (R + G + B) / 3</strong>
</p>

**R.:**


Sabendo que, para CMYK e K $\ne$ 1, temos:


<p align="center">
  C = (1 - R - K) / (1 - K)
</p>

manipulando, nos temos:

<p align="center">
  C = (1 - R - K) / (1 - K) = [(1 - K) / (1 - K)] - R / (1 - K) = 1 - R / (1 - K)
</p>

dado já que K $\ne$ 1, temos tambem que:

<p align="center">
  1 - K &ge;  R &rarr; - K  &ge; R - 1 &rarr; K &le; 1 - R
</p>



analogo, temos que:


<table align="center" style="border-collapse: collapse; text-align: left;">
  <tr>
    <td>K &leq; 1 - R, para C</td>
  </tr>
  <tr>
    <td>K &leq; 1 - G, para M</td>
  </tr>
  <tr>
    <td>K &leq; 1 - B, para Y</td>
  </tr>
</table>

portanto, K &le; min{1 - R, 1 - G, 1 - B}. Dado isso, e aplicando a formula definida na questão, temos (fixando primeiro C, analogo para os outros):

<table align="center" style="border-collapse: collapse; text-align: left;">
  <tr>
    <td>1 - (R + G + B) / 3 &leq; 1 - R</td>
  </tr>
  <tr>
    <td>(R + G + B) / 3 &geq; R</td>
  </tr>
  <tr>
    <td>R + G + B &geq; 3 &times; R</td>
  </tr>
  <tr>
    <td>G + B &geq; 2 &times; R</td>
  </tr>
</table>

analogo, por fim, temos as condições para que 1 - K &ge; R, para C, analogo para MY, que:

<p style="text-align: center;">
    G + B &ge; 2 &times; R
</p>

<p style="text-align: center;">
    logo:
</p>

<table align="center" style="border-collapse: collapse; text-align: center;">
    <tr>
        <td>G + B &ge; 2 &times; R, para C</td>
    </tr>
    <tr>
        <td>R + B &ge; 2 &times; G, para M</td>
    </tr>
    <tr>
        <td>G + R &ge; 2 &times; B, para Y</td>
    </tr>
</table>

Alem disso, esse cálculo pode levar  um preto ainda mais forte do que oque realmente deveria ser, por exemplo, suponha o cenário aonde temos um (R, G, B) = (120, 40, 100), ou seja, em escala normalizada temos (0.47, 0.16, 0.39), vamos calcular K pelo espaço CMYK e por esse apresentado na questão:


* **CMYK**

<p align="center">
  K = 1 - max(R, G, B) = 1 - max(0.47, 0.16, 0.39) = 1 - 0.47 = 0.53
</p>

* **Explicitado pela questão**

<p align="center">
K = 1 - (R + G + B) / 3 = 1 - (0.47 + 0.16 + 0.39) / 3 = 1 - 0.34 = 0.66
</p>


nesse caso podemos notar um enfase na tonalidade do preto, enfatizando ainda mais, podendo prejudicar a visualização da imagem, com o preto em maior enfase, ou seja, imagens um pouco mais escuras, com menores valores de R, G e B podem ser consequentemente transformadas em tons mais escuros devido a essa transformação.


# Questão 04

**Considere o vetor abaixo como a representação de uma imagem. O valor em 
cada célula dele representa um tom de cinza, para uma imagem armazenada em 
256 tons de cinza:**

<p align="center">
[10, 20, 10, 50, 40, 40, 20, 20, 10, 10]
</p>

**Calcule a imagem resultante de um processo de equalização, conforme 
estabelecido no slide 62 da aula de Codificação de cores. Apresente todos os 
cálculos. Considere seu resultado anterior. Aplique novamente a mesma operação de 
equalização. Novamente, apresente todos os cálculos. O que aconteceu com o 
resultado? Justifique.**


**R.:** 

Sabendo-se que a forma para equallização é a abaixo:

<p align="center">
  k = &sum;<sup>j</sup><sub>i = 0</sub>N<sub>i</sub> / T
</p>


* **1º equalização**

    * **Vetor original**: [10, 20, 10, 50, 40, 40, 20, 20, 10, 10]

    Logo, multiplicando por 255, temos os novos valores equalizados. Então, temos os valores abaixo:


    | j  | Nᵢ / T       | 255 &times; Nᵢ / T  |
    |----|------------|----------------|
    | 10 | 4 / 10 = 0.4  | 0.4 &times; 255 = 102  |
    | 20 | (4 / 10) + (3 / 10) = 0.7  | 0.7 &times; 255 &approx; 178.5 &approx; 179   |
    | 40 | (4 / 10) + (3 / 10) + (2 / 10) = 0.9  | 0.9 &times; 255 &approx; 229.5 &approx; 230|
    | 50 | (4 / 10) + (3 / 10) + (2 / 10) + (1 / 10) = 1  | 1 &times; 255 = 255  |

    Então, temos o novo vetor equalizado abaixo


    * **Vetor equalizado**: [102, 179, 102, 255, 230, 230, 179, 179, 102, 102]

* **2º equalização**

    * **Vetor obtido da 1ª equalização**: [102, 179, 102, 255, 230, 230, 179, 179, 102, 102]

    Logo, multiplicando por 255, temos os novos valores equalizados. Então, temos os valores abaixo:

    | j   | Nᵢ / T       | 255 &times; Nᵢ / T  |
    |-----|------------|----------------|
    | 102 | 4 / 10 = 0.4  | 0.4 &times; 255 = 102  |
    | 179 | (4 / 10) + (3 / 10) = 0.7  | 0.7 &times; 255 &approx; 178.5 &approx; 179   |
    | 230 | (4 / 10) + (3 / 10) + (2 / 10) = 0.9  | 0.9 &times; 255 &approx; 229.5 &approx; 230|
    | 255 | (4 / 10) + (3 / 10) + (2 / 10) + (1 / 10) = 1  | 1 &times; 255 = 255  |

    Então, temos o novo vetor equalizado abaixo:

    * **Vetor final**: [102, 179, 102, 255, 230, 230, 179, 179, 102, 102]

* **Conclusão 1º equalização**: A primeira equalização deixou as cores mais claras ainda mais claras, com uma diferença maior para as cores mais escuras, assim como as escuras ainda mais escura, oque era esperado devido a natureza da propria equalização.

* **Conclusão 2º equalização**: Nota-se que após a segunda equalização os valores permaneceram os mesmos, uma vez que a primeira equalização já distribuiu os tons de forma uniforme na primeira aplicação, fazendo com que a segunda equalização não fosse mais necessária.

* **Imagem anexo**

![q4](https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q04.png?raw=true)

# Questão 05

**Repita a questão anterior aplicando a correção gamma apresentada no slide 67 
da aula de Codificação de Cores com &gamma; = 3 e c = 1, na mesma imagem dada. 
Trabalhe com duas abordagens diferentes:**

**a) Na primeira, considere normalizar (e "desnormalizar") a imagem por 255.**

**b) Na segunda, considere normalizar (e "desnormalizar") a imagem pelo máximo tom presente nela (no caso 50).**

**Qual a diferença entre os dois resultados finais?**

**R.:**

Consideraremos &gamma; = 3 e c = 1, além disso, a formula para a transformação &gamma; pode ser expressa abaixo:


<p align="center">
lm<sub>out</sub> = c &times; (lm<sub>in</sub>)<sup>&gamma;</sup>
</p>


e as normalizações e desnormalizações para cada item serão:

* Para o item **A**, temos a normalização r = x / 255  e a desnormalização expressa por x = r &times; 255

* Para o item **B**, temos a normalização r = x / 50  e a desnormalização expressa por x = r &times; 50


## **Item a)**: 


Considerando o vetor original [10, 20, 10, 50, 40, 40, 20, 20, 10, 10], vamos contruir uma tabela para facilitar os calculos, tal qual como feito na questão 04, logo:



| x | r = x / 255 | lm<sub>out</sub> = 1 &times; (lm<sub>in</sub>)<sup>3</sup> | x = r &times; 255 |
|----|--------------|--------------|----------------|
| 10 | 0.0392      | 1 &times; (0.0392)<sup>3</sup> = 0.0000603 | 0.0000603 &times; 255 = 0.0154 &approx; 0 |
| 20 | 0.0784      | 1 &times; (0.0784)<sup>3</sup> = 0.0004828 | 0.0004828 &times; 255 = 0.1231 &approx; 0 |
| 40 | 0.1569      | 1 &times; (0.1569)<sup>3</sup> = 0.003862  | 0.003862 &times; 255 = 0.9848 &approx; 1 |
| 50 | 0.1961      | 1 &times; (0.1961)<sup>3</sup> = 0.007544  | 0.007544 &times; 255 = 1.9247 &approx;  2 |


Logo, o vetor final obtido apartir da correção gama pode ser dado por:

<p align="center">
[0, 0, 0, 2, 1, 1, 0, 0, 0, 0]
<p>

* **Representação da imagem**:

![q05-a](https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q05-01.png?raw=true)

## **Item b)**: 


Considerando o vetor original [10, 20, 10, 50, 40, 40, 20, 20, 10, 10], vamos contruir uma tabela para facilitar os calculos, como no item **a**, logo:

| x | r = x / 50 | lm<sub>out</sub> = 1 &times; (lm<sub>in</sub>)<sup>3</sup> | x = r &times; 50 |
|----|--------------|--------------|----------------|
| 10 | 0.2      | 1 &times; (0.2)<sup>3</sup> = 0.008 | 0.008 &times; 50 = 0.4 &approx; 0 |
| 20 | 0.4      | 1 &times; (0.4)<sup>3</sup> = 0.064 | 0.064 &times; 50 = 3.2 &approx; 3 |
| 40 | 0.8      | 1 &times; (0.8)<sup>3</sup> = 0.512  | 0.512 &times; 50 = 25.6 &approx; 26 |
| 50 | 1.0      | 1 &times; (1.0)<sup>3</sup> = 1.0  | 1.0 &times; 50 = 50.0 &approx;  50 |


Logo, o vetor final obtido apartir da correção gama pode ser dado por:

<p align="center">
[0, 3, 0, 50, 26, 26, 3, 3, 0, 0]
<p>

* **Representação da imagem**:

![q05-b](https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q05-02.png?raw=true)

## Comparando resultados de ambos:

![q05-ambas](https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q05-03.png?raw=true)


Para o item **a**, tiveram muitos valores 0, acarretando em um destque da imagem em preto, escurecendo mais o  tom preto, pedendo detalhe e não podendo distinguir cor mais algumas entradas do vetor, uma vez que ficou mais uniforme.

Para o item **b**, podemos notar um aumento das cores mais escuras, sendo os tons cinza mais escuro mais enfatizados, tornando ainda mais pretos, contudo ainda possivel distinguir trechos da imagem.

Nesse exemplo podemos ver claramente o efeito do &gamma; > 1 ocorrendo, uma vez que comprimiu valores de intensidade mais baixos, aumentando o destaque sobre o preto.


# Questão 06

<strong>As matrizes abaixo correspondem às componentes RGB de uma imagem. </strong>

<table>
  <tr>
    <td>
      <strong>R</strong>
      <table>
        <tr><td>255</td><td>240</td><td>200</td><td>150</td><td>120</td></tr>
        <tr><td>230</td><td>220</td><td>180</td><td>160</td><td>100</td></tr>
        <tr><td>210</td><td>190</td><td>170</td><td>145</td><td>90</td></tr>
        <tr><td>170</td><td>160</td><td>140</td><td>130</td><td>80</td></tr>
        <tr><td>185</td><td>165</td><td>155</td><td>135</td><td>122</td></tr>
      </table>
    </td>
    <td>
      <strong>G</strong>
      <table>
        <tr><td>255</td><td>240</td><td>230</td><td>235</td><td>210</td></tr>
        <tr><td>240</td><td>245</td><td>250</td><td>255</td><td>180</td></tr>
        <tr><td>230</td><td>220</td><td>0</td><td>230</td><td>200</td></tr>
        <tr><td>240</td><td>245</td><td>250</td><td>255</td><td>180</td></tr>
        <tr><td>255</td><td>240</td><td>230</td><td>235</td><td>210</td></tr>
      </table>
    </td>
    <td>
      <strong>B</strong>
      <table>
        <tr><td>255</td><td>255</td><td>200</td><td>180</td><td>160</td></tr>
        <tr><td>240</td><td>230</td><td>190</td><td>140</td><td>120</td></tr>
        <tr><td>245</td><td>235</td><td>0</td><td>180</td><td>160</td></tr>
        <tr><td>240</td><td>230</td><td>190</td><td>140</td><td>120</td></tr>
        <tr><td>255</td><td>255</td><td>200</td><td>180</td><td>160</td></tr>
      </table>
    </td>
  </tr>
</table>

<strong>
Calcule a imagem em tons de cinza resultante para essas três matrizes, criada: 

a) através da Média; 

b) através do uso de pesos conforme o slide 47 da aula de Modelos de cores. 

c) Através do cálculo da dessaturação, como abaixo: 

    Tom_cinza = [max(R, G, B) + min(R, G, B)]/2 
</strong>

**R.:**

Primeiro, vamos visualizar a matriz formada pela combinação de R, G e B, dada abaixo:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q06-01.png?raw=true" alt="q06-01" width="400"/>
</p>


## Item A) 

Vamos aplicar a média dos termos, então temos:

<p>
    Z = (R + G + B) / 3 = (R / 3) + (G / 3) + (B / 3)
</p>


Onde:

<div style="display: flex;">
R / 3 = 
  <table>
    <tr>
      <td>(255/3)</td><td>(240/3)</td><td>(200/3)</td><td>(150/3)</td><td>(120/3)</td>
    </tr>
    <tr>
      <td>(230/3)</td><td>(220/3)</td><td>(180/3)</td><td>(160/3)</td><td>(100/3)</td>
    </tr>
    <tr>
      <td>(210/3)</td><td>(190/3)</td><td>(170/3)</td><td>(145/3)</td><td>(90/3)</td>
    </tr>
    <tr>
      <td>(170/3)</td><td>(160/3)</td><td>(140/3)</td><td>(130/3)</td><td>(80/3)</td>
    </tr>
    <tr>
      <td>(185/3)</td><td>(165/3)</td><td>(155/3)</td><td>(135/3)</td><td>(122/3)</td>
    </tr>
  </table>
  = 
    <table>
    <tr>
        <td>85</td><td>80</td><td>67</td><td>50</td><td>40</td>
    </tr>
    <tr>
        <td>77</td><td>73</td><td>60</td><td>53</td><td>33</td>
    </tr>
    <tr>
        <td>70</td><td>63</td><td>57</td><td>48</td><td>30</td>
    </tr>
    <tr>
        <td>57</td><td>53</td><td>47</td><td>43</td><td>27</td>
    </tr>
    <tr>
        <td>62</td><td>55</td><td>52</td><td>45</td><td>41</td>
    </tr>
    </table>
</div>



<div style="display: flex;">
G / 3 = 
  <table>
    <tr>
      <td>(255/3)</td><td>(240/3)</td><td>(230/3)</td><td>(235/3)</td><td>(210/3)</td>
    </tr>
    <tr>
      <td>(240/3)</td><td>(245/3)</td><td>(250/3)</td><td>(255/3)</td><td>(180/3)</td>
    </tr>
    <tr>
      <td>(230/3)</td><td>(220/3)</td><td>(0/3)</td><td>(230/3)</td><td>(200/3)</td>
    </tr>
    <tr>
      <td>(240/3)</td><td>(245/3)</td><td>(250/3)</td><td>(255/3)</td><td>(180/3)</td>
    </tr>
    <tr>
      <td>(255/3)</td><td>(240/3)</td><td>(230/3)</td><td>(235/3)</td><td>(210/3)</td>
    </tr>
  </table>
  = 
  <table>
    <tr>
        <td>85</td><td>80</td><td>77</td><td>78</td><td>70</td>
    </tr>
    <tr>
        <td>80</td><td>82</td><td>83</td><td>85</td><td>60</td>
    </tr>
    <tr>
        <td>77</td><td>73</td><td>0</td><td>77</td><td>67</td>
    </tr>
    <tr>
        <td>80</td><td>82</td><td>83</td><td>85</td><td>60</td>
    </tr>
    <tr>
        <td>85</td><td>80</td><td>77</td><td>78</td><td>70</td>
    </tr>
  </table>
</div>


<div style="display: flex;">
B / 3 = 
  <table>
    <tr>
      <td>(255/3)</td><td>(255/3)</td><td>(200/3)</td><td>(180/3)</td><td>(160/3)</td>
    </tr>
    <tr>
      <td>(240/3)</td><td>(230/3)</td><td>(190/3)</td><td>(140/3)</td><td>(120/3)</td>
    </tr>
    <tr>
      <td>(245/3)</td><td>(235/3)</td><td>(0/3)</td><td>(180/3)</td><td>(160/3)</td>
    </tr>
    <tr>
      <td>(240/3)</td><td>(230/3)</td><td>(190/3)</td><td>(140/3)</td><td>(120/3)</td>
    </tr>
    <tr>
      <td>(255/3)</td><td>(255/3)</td><td>(200/3)</td><td>(180/3)</td><td>(160/3)</td>
    </tr>
  </table>
  = 
  <table>
    <tr>
        <td>85</td><td>85</td><td>67</td><td>60</td><td>53</td>
    </tr>
    <tr>
        <td>80</td><td>77</td><td>63</td><td>47</td><td>40</td>
    </tr>
    <tr>
        <td>82</td><td>78</td><td>0</td><td>60</td><td>53</td>
    </tr>
    <tr>
        <td>80</td><td>77</td><td>63</td><td>47</td><td>40</td>
    </tr>
    <tr>
        <td>85</td><td>85</td><td>67</td><td>60</td><td>53</td>
    </tr>
  </table>
</div>


Logo, temos que:


<div style="display: flex;">
Z = (R + G + B) / 3 = (R / 3) + (G / 3) + (B / 3) = 
  <table>
    <tr>
        <td>255</td><td>245</td><td>210</td><td>188</td><td>163</td>
    </tr>
    <tr>
        <td>237</td><td>232</td><td>207</td><td>185</td><td>133</td>
    </tr>
    <tr>
        <td>228</td><td>215</td><td>57</td><td>185</td><td>150</td>
    </tr>
    <tr>
        <td>217</td><td>212</td><td>193</td><td>175</td><td>127</td>
    </tr>
    <tr>
        <td>232</td><td>220</td><td>195</td><td>183</td><td>164</td>
    </tr>
  </table>
</div>

Resultando na imagem:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q06-02.png?raw=true" alt="q06-02" width="400"/>
</p>


## Item B)

Para esse item, vamos considerar os mesmo pesos utilizados no slide 47 de exemplo (0.29, 0.59, 0.11). Então:

<div style="display: flex;">
R &times; 0.29 = 
  <table>
    <tr>
      <td>(255 &times; 0.29)</td><td>(240 &times; 0.29)</td><td>(200 &times; 0.29)</td><td>(150 &times; 0.29)</td><td>(120 &times; 0.29)</td>
    </tr>
    <tr>
      <td>(230 &times; 0.29)</td><td>(220 &times; 0.29)</td><td>(180 &times; 0.29)</td><td>(160 &times; 0.29)</td><td>(100 &times; 0.29)</td>
    </tr>
    <tr>
      <td>(210 &times; 0.29)</td><td>(190 &times; 0.29)</td><td>(170 &times; 0.29)</td><td>(145 &times; 0.29)</td><td>(90 &times; 0.29)</td>
    </tr>
    <tr>
      <td>(170 &times; 0.29)</td><td>(160 &times; 0.29)</td><td>(140 &times; 0.29)</td><td>(130 &times; 0.29)</td><td>(80 &times; 0.29)</td>
    </tr>
    <tr>
      <td>(185 &times; 0.29)</td><td>(165 &times; 0.29)</td><td>(155 &times; 0.29)</td><td>(135 &times; 0.29)</td><td>(122 &times; 0.29)</td>
    </tr>
  </table>
  = 
    <table>
     <tr>
        <td>74</td><td>70</td><td>58</td><td>44</td><td>35</td>
    </tr>
    <tr>
        <td>67</td><td>64</td><td>52</td><td>46</td><td>29</td>
    </tr>
    <tr>
        <td>61</td><td>55</td><td>49</td><td>42</td><td>26</td>
    </tr>
    <tr>
        <td>49</td><td>46</td><td>41</td><td>38</td><td>23</td>
    </tr>
    <tr>
        <td>54</td><td>48</td><td>45</td><td>39</td><td>35</td>
    </tr>
    </table>
</div>



<div style="display: flex;">
G &times; 0.59 = 
  <table>
    <tr>
      <td>(255 &times; 0.59)</td><td>(240 &times; 0.59)</td><td>(230 &times; 0.59)</td><td>(235 &times; 0.59)</td><td>(210 &times; 0.59)</td>
    </tr>
    <tr>
      <td>(240 &times; 0.59)</td><td>(245 &times; 0.59)</td><td>(250 &times; 0.59)</td><td>(255 &times; 0.59)</td><td>(180 &times; 0.59)</td>
    </tr>
    <tr>
      <td>(230 &times; 0.59)</td><td>(220 &times; 0.59)</td><td>(0 &times; 0.59)</td><td>(230 &times; 0.59)</td><td>(200 &times; 0.59)</td>
    </tr>
    <tr>
      <td>(240 &times; 0.59)</td><td>(245 &times; 0.59)</td><td>(250 &times; 0.59)</td><td>(255 &times; 0.59)</td><td>(180 &times; 0.59)</td>
    </tr>
    <tr>
      <td>(255 &times; 0.59)</td><td>(240 &times; 0.59)</td><td>(230 &times; 0.59)</td><td>(235 &times; 0.59)</td><td>(210 &times; 0.59)</td>
    </tr>
  </table>
  = 
  <table>
    <tr>
        <td>150</td><td>142</td><td>136</td><td>139</td><td>124</td>
    </tr>
    <tr>
        <td>142</td><td>145</td><td>148</td><td>150</td><td>106</td>
    </tr>
    <tr>
        <td>136</td><td>130</td><td>0</td><td>136</td><td>118</td>
    </tr>
    <tr>
        <td>142</td><td>145</td><td>148</td><td>150</td><td>106</td>
    </tr>
    <tr>
        <td>150</td><td>142</td><td>136</td><td>139</td><td>124</td>
    </tr>
  </table>
</div>


<div style="display: flex;">
B &times; 0.11 = 
  <table>
    <tr>
      <td>(255 &times; 0.11)</td><td>(255 &times; 0.11)</td><td>(200 &times; 0.11)</td><td>(180 &times; 0.11)</td><td>(160 &times; 0.11)</td>
    </tr>
    <tr>
      <td>(240 &times; 0.11)</td><td>(230 &times; 0.11)</td><td>(190 &times; 0.11)</td><td>(140 &times; 0.11)</td><td>(120 &times; 0.11)</td>
    </tr>
    <tr>
      <td>(245 &times; 0.11)</td><td>(235 &times; 0.11)</td><td>(0 &times; 0.11)</td><td>(180 &times; 0.11)</td><td>(160 &times; 0.11)</td>
    </tr>
    <tr>
      <td>(240 &times; 0.11)</td><td>(230 &times; 0.11)</td><td>(190 &times; 0.11)</td><td>(140 &times; 0.11)</td><td>(120 &times; 0.11)</td>
    </tr>
    <tr>
      <td>(255 &times; 0.11)</td><td>(255 &times; 0.11)</td><td>(200 &times; 0.11)</td><td>(180 &times; 0.11)</td><td>(160 &times; 0.11)</td>
    </tr>
  </table>
  = 
  <table>
    <tr>
        <td>28</td><td>28</td><td>22</td><td>20</td><td>18</td>
    </tr>
    <tr>
        <td>26</td><td>25</td><td>21</td><td>15</td><td>13</td>
    </tr>
    <tr>
        <td>27</td><td>26</td><td>0</td><td>20</td><td>18</td>
    </tr>
    <tr>
        <td>26</td><td>25</td><td>21</td><td>15</td><td>13</td>
    </tr>
    <tr>
        <td>28</td><td>28</td><td>22</td><td>20</td><td>18</td>
    </tr>
  </table>
</div>


Logo, temos que:


<div style="display: flex;">
Z = (R &times; 0.29) + (G &times; 0.59) + (B &times; 0.11) = 
  <table>
    <tr>
        <td>252</td><td>240</td><td>216</td><td>203</td><td>177</td>
    </tr>
    <tr>
        <td>235</td><td>234</td><td>221</td><td>211</td><td>148</td>
    </tr>
    <tr>
        <td>224</td><td>211</td><td>49</td><td>198</td><td>162</td>
    </tr>
    <tr>
        <td>217</td><td>216</td><td>210</td><td>203</td><td>142</td>
    </tr>
    <tr>
        <td>232</td><td>218</td><td>203</td><td>198</td><td>177</td>
    </tr>
  </table>
</div>

Gerando a imagem abaixo:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q06-03.png?raw=true" alt="q06-03" width="400"/>
</p>

<br>
<br>
<br>

## Item C)


<div style="display: flex;">
Z = [max(R, G, B) + min(R, G, B)] / 2 = 
  <table>
    <tr>
      <td>(255 + 255) / 2</td><td>(255 + 240) / 2</td><td>(230 + 200) / 2</td><td>(235 + 150) / 2</td><td>(210 + 120) / 2</td>
    </tr>
    <tr>
      <td>(240 + 230) / 2</td><td>(245 + 220) / 2</td><td>(250 + 180) / 2</td><td>(255 + 140) / 2</td><td>(180 + 100) / 2</td>
    </tr>
    <tr>
      <td>(245 + 210) / 2</td><td>(235 + 190) / 2</td><td>(170 + 0) / 2</td><td>(230 + 145) / 2</td><td>(200 + 90) / 2</td>
    </tr>
    <tr>
      <td>(240 + 170) / 2</td><td>(245 + 160) / 2</td><td>(250 + 140) / 2</td><td>(255 + 130) / 2</td><td>(180 + 80) / 2</td>
    </tr>
    <tr>
      <td>(255 + 185) / 2</td><td>(255 + 165) / 2</td><td>(230 + 155) / 2</td><td>(235 + 135) / 2</td><td>(210 + 122) / 2</td>
    </tr>
  </table>
  = 
  <table>
    <tr>
        <td>255</td><td>247</td><td>215</td><td>192</td><td>165</td>
    </tr>
    <tr>
        <td>235</td><td>232</td><td>215</td><td>197</td><td>140</td>
    </tr>
    <tr>
        <td>227</td><td>212</td><td>85</td><td>187</td><td>145</td>
    </tr>
    <tr>
        <td>205</td><td>202</td><td>195</td><td>192</td><td>130</td>
    </tr>
    <tr>
        <td>220</td><td>210</td><td>192</td><td>185</td><td>166</td>
    </tr>
  </table>
</div>

Gerando a imagem abaixo:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q06-04.png?raw=true" alt="q06-04" width="400"/>
</p>

## Conclusão

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q06-05.png?raw=true" alt="q06-05" width="1200"/>
</p>

A ponderação deu uma clareada maior, em geral, na imagem, diferentemente dos outros metodos, como o uso da média, que apresenta uma coloração mais homogenea, mas sem enfatizar muito o branco e  o preto. Já a dessaturação parece retratar melhor detalhes das cores da imagem, enfatizando melhor o preto.

# Questão 07

<strong>
Considere a imagem IM abaixo em 256 tons de cinza no sistema RGB: 
</strong>

<table align="center" border="1" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>120</td>
    <td>140</td>
    <td>120</td>
  </tr>
  <tr>
    <td>160</td>
    <td>180</td>
    <td>70</td>
  </tr>
</table>

<strong>
Considere a versão reduzida da matriz de Floyd-Steinberg: 


<div style="text-align: center;">
    <p>
        <span style="font-size: 1.5em;">(1 / 16) &times; </span>
        <table style="display: inline-table; border-spacing: 0; border-collapse: collapse;">
            <tr>
                <td style="border: 1px solid black; padding: 5px;">0</td>
                <td style="border: 1px solid black; padding: 5px;">X</td>
                <td style="border: 1px solid black; padding: 5px;">7</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 5px;">3</td>
                <td style="border: 1px solid black; padding: 5px;">5</td>
                <td style="border: 1px solid black; padding: 5px;">1</td>
            </tr>
        </table>
    </p>
</div>

onde X marca o pixel sendo processado. Em uma implementação, X pode ser 
substituído por zero, já que o que importa é a porcentagem do erro transmitido aos 
vizinhos.

Calcule a imagem binarizada resultante do uso da máscara de Floyd-Steinberg em 
IM, considerando 127 como ponto de corte. Apresente todos os cálculos.</strong>


**R.:**



Vamos processar, começando pelo pixel P(0, 0) = 120, logo:

1) <strong>P(0, 0) temos: </strong>
<p align="center">
  P(0, 1) = 140 + 120 &times; 7/16 = 193  
  <br>
  P(1, 0) = 160 + 120 &times; 5/16 = 198  
  <br>
  P(1, 1) = 180 + 120 &times; 1/16 = 188
</p>

Logo, temos:

<table align="center" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>0</td>
    <td>193</td>
    <td>120</td>
  </tr>
  <tr>
    <td>198</td>
    <td>188</td>
    <td>70</td>
  </tr>
</table>

2) <strong>Para P(0, 1), temos:</strong>

<p align="center">
P(0, 2) = 120 + (-63) &times; 7/16 = 93  
<br>
P(1, 0) = 198 + (-63) &times; 3/16 = 186  
<br>
P(1, 1) = 188 + (-63) &times; 5/16 = 168  
<br>
P(1, 2) = 70 + (-63) &times; 1/16 = 66  
</p>

Logo, temos:


<table align="center" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>0</td>
    <td>255</td>
    <td>93</td>
  </tr>
  <tr>
    <td>186</td>
    <td>168</td>
    <td>66</td>
  </tr>
</table>

3) <strong>Para P(0, 2), temos:</strong>

<p align="center">
  P(1, 1) = 168 + 93 &times; 3/16 = 185  
  <br>
  P(1, 2) = 66 + 93 &times; 5/16 = 95  
</p>

Logo, temos:

<table align="center" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>0</td>
    <td>255</td>
    <td>0</td>
  </tr>
  <tr>
    <td>186</td>
    <td>185</td>
    <td>95</td>
  </tr>
</table>


4) <strong>Para P(1, 0), temos:</strong>

<p align="center">
  P(1, 1) = 185 + (-69) &times; 7/16 = 155
</p>

Logo, temos:

<table align="center" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>0</td>
    <td>255</td>
    <td>0</td>
  </tr>
  <tr>
    <td>255</td>
    <td>155</td>
    <td>95</td>
  </tr>
</table>

5) <strong>Para P(1, 1), temos:</strong>

<p align="center">
  P(1, 2) = 95 + (-100) &times; 7/16 = 51
</p>

Logo, temos:

<table align="center" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>0</td>
    <td>255</td>
    <td>0</td>
  </tr>
  <tr>
    <td>255</td>
    <td>255</td>
    <td>51</td>
  </tr>
</table>

6) <strong>Para P(1, 2), temos:</strong>

Como P(1, 2) = 51 < 127, e ultima entrada, então podemos atribuir 0 direto.

Logo, temos:

<table align="center" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>0</td>
    <td>255</td>
    <td>0</td>
  </tr>
  <tr>
    <td>255</td>
    <td>255</td>
    <td>0</td>
  </tr>
</table>

## Conclusão

A matriz binarizada pode ser encontrada abaixo:

<table align="center" style="border-collapse: collapse; text-align: center;">
  <tr>
    <td>0</td>
    <td>255</td>
    <td>0</td>
  </tr>
  <tr>
    <td>255</td>
    <td>255</td>
    <td>0</td>
  </tr>
</table>

Podemos comparar a imagem original versus a binarizada da mascara de Floyd-Steinberg abaixo:


<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv04-q07-01.png?raw=true" alt="q06-05" width="1200"/>
</p>

# Questão 08


<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/q08-img.png?raw=true" alt="q08-img" width="1200"/>
</p>
