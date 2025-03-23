# Atividade: Teoria da Utilidade


* **Aluno:** Manuel Ferreira Junior
* **Disciplina:** Processamento Digital de Imagens

# Questão 03:

**Sabendo que o modelo CMYK é usado em dispositivos de impressão e que 
cada valor de Ciano (C), Magenta (M), Amarelo (Y) e Preto (K) correspondem a 
uma quantidade de tinta a ser usada na mistura para impressão, gerando 
diferentes cores. Considerando a conversão de RGB para CMYK apresentada no 
slide 18 da aula de Modelos de Cores, que problema poderíamos ter se o cálculo 
da componente K fosse dado como abaixo?** 

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


# Questão 04:

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

![q4](/assets/atv04-q04.png)

# Questão 05:

**Repita a questão anterior aplicando a correção gamma apresentada no slide 67 
da aula de Codificação de Cores com &gamma; = 3 e c = 1, na mesma imagem dada. 
Trabalhe com duas abordagens diferentes:**

**a) Na primeira, considere normalizar (e "desnormalizar") a imagem por 255.**

**b) Na segunda, considere normalizar (e "desnormalizar") a imagem pelo máximo tom presente nela (no caso 50).**

**Qual a diferença entre os dois resultados finais?**

**R.:**