# Atividade 01

* **Aluno:** Manuel Ferreira Junior
* **Disciplina:** Processamento Digital de Imagens

# Questão 03

**Sabendo que o modelo CMYK é usado em dispositivos de impressão e que 
cada valor de Ciano (C), Magenta (M), Amarelo (Y) e Preto (K) correspondem a 
uma quantidade de tinta a ser usada na mistura para impressão, gerando 
diferentes cores. Considerando a conversão de RGB para CMYK apresentada no 
slide 18 da aula de Modelos de Cores, que problema p2oderíamos ter se o cálculo 
da componente K fosse dado como abaixo?** 

<p align="center">
<strong>K = 1 - (R + G + B) / 3</strong>
</p>

**R.:** Considerando que R, G e B estão em escala normalizada e K deve representar o preto, esse cálculo pode levar  um preto ainda mais forte do que oque realmente deveria ser, por exemplo, suponha o cenário aonde temos um (R, G, B) = (120, 40, 100), ou seja, em escala normalizada temos (0.47, 0.16, 0.39), vamos calcular K pelo espaço CMYK e por esse apresentado na questão:


* **CMYK**

<p align="center">
  K = 1 - max(R, G, B) = 1 - max(0.47, 0.16, 0.39) = 1 - 0.47 = 0.53
</p>

* **Explicitado pela questão**

<p align="center">
K = 1 - (R + G + B) / 3 = 1 - (0.47 + 0.16 + 0.39) / 3 = 1 - 0.34 = 0.66
</p>


nesse caso podemos notar um enfase na tonalidade do preto, enfatizando ainda mais, podendo prejudicar a visualização da imagem, com o preto em maior enfase, ou seja, imagens um pouco mais escuras, com menores valores de R, G e B podem ser consequente transformadas em tons ainda mais escuros devido a essa transformação. Um outro exemplo, seria o caso (R, G, B) = (0.4, 0.3, 0.2), que para a escala CMYK, teremos K = 0.4, mas pela transformação em questão teremos K = 1 - (0.4 + 0.3 + 0.2)/ 3 = 1 - 0.3 = 0.7.


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



| x | r = x / 255 | lm<sub>out</sub> = 1 &times; (lm<sub>in</sub>)<sup>3</sup> | x = r \times 255 |
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

