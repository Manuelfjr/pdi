<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML-full">
</script>

# Atividade 02

* **Aluno:** Manuel Ferreira Junior
* **Disciplina:** Processamento Digital de Imagens

* **Obs. (1):** Questões com necessidade de calculo de convolução, estarão todas as expressões no [link](https://docs.google.com/spreadsheets/d/1cWB3zNBbDXzFNvEKotBCVPIlnS8cde-SXRjCP55ISTM/edit?usp=sharing), para facilitar a visualização e leitura da atividade. Além disso, cada questão em anexo possui uma copia da sua operação que deve ser realizada. Cada sheet do link em anexo, possui no seu titulo a questão referente e operação referente.

* **Obs. (2):** Com respeito as questões de implementação (8, 9 e 10), além do código disponibilizado no pdf, os links para os notebooks utilizados para as aplicações estão abaixo:

  1) `Questão 08:` 
     * `Solução 01:` [02_01_atv02_code_q08_sol1](https://github.com/Manuelfjr/pdi/blob/develop/notebooks/02_01_atv02_code_q08_sol1.ipynb)
     * `Solução 02:` [02_02_atv02_code_q08_sol2](https://github.com/Manuelfjr/pdi/blob/develop/notebooks/02_02_atv02_code_q08_sol2.ipynb)
  
  2) `Questão 09:` [03_atv02_code_q09](https://github.com/Manuelfjr/pdi/blob/develop/notebooks/03_atv02_code_q09.ipynb)

  3) `Questão 10:` [04_atv02_code_q10](https://github.com/Manuelfjr/pdi/blob/develop/notebooks/04_atv02_code_q10.ipynb)

  4) `[Rascunhos para validação de resoluções] Códigos para outras questões:` [01_atv02_code](https://github.com/Manuelfjr/pdi/blob/develop/notebooks/01_atv02_code.ipynb)

# Imports

```py
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.signal import convolve2d
from scipy.fft import ifft2
```

# Funções 

Abaixo, temos as funções criadas para utilizar ao decorrer da atividade, para as questões de implementação.

```py
def find_contorno(imagem):
    """Verifica se a imagem contém a letra A maiúscula"""
    # Binariza a imagem (inversão: fundo branco, letras pretas)
    _, img_bin = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Encontra contornos (possíveis letras)
    contornos, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contornos, img_bin

def tm_ccoef_normed(image: np.ndarray, template: np.ndarray) -> np.ndarray:
    """
    Calcula a correlação cruzada normalizada (TM_CCOEFF_NORMED) entre a imagem e o template.

    Parâmetros:
    - image: imagem de entrada (2D, em escala de cinza)
    - template: template a ser comparado (2D, em escala de cinza)

    Retorna:
    - result: mapa de similaridade (valores entre -1 e 1)
    """
    img_h, img_w = image.shape
    tpl_h, tpl_w = template.shape

    # Média e T' do template
    template_mean = np.mean(template)
    template_prime = template - template_mean
    template_prime_squared_sum = np.sum(template_prime ** 2)

    # Saída terá tamanho reduzido
    result_h = img_h - tpl_h + 1
    result_w = img_w - tpl_w + 1
    result = np.zeros((result_h, result_w), dtype=np.float32)

    # Para cada posição possível (x, y) na imagem:
    for y in range(result_h):
        for x in range(result_w):
            region = image[y:(y + tpl_h), x:(x + tpl_w)]
            region_mean = np.mean(region)
            region_prime = region - region_mean
            region_prime_squared_sum = np.sum(region_prime ** 2)

            numerator = np.sum(template_prime * region_prime)
            denominator = np.sqrt(template_prime_squared_sum * region_prime_squared_sum)

            result[y, x] = numerator / denominator if denominator != 0 else 0.0

    return result
```

# Questão 01

<strong>
A imagem da esquerda tem a magnitude da sua transformada de Fourier 
apresentada à direita:

</strong>

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q01-01.png?raw=true" alt="q01-i1-img" width="600"/>
</p>

<strong>
Como deve ser a mesma figura da magnitude da transformada de Fourier para as imagens abaixo? Considere que a única mudança, em relação à imagem apresentada acima e à esquerda, é o deslocamento do bloco branco. Justifique sua resposta. 

Obs: Você não tem a imagem original para calcular a transformada. Apenas 
especule sobre o resultado esperado. 
</strong>

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q01-02.png?raw=true" alt="q01-i2-img" width="600"/>
</p>


**R.:**

A Transformada de Fourier tem como foco principal analisar a distribuicao das frequências da iamgem e não elementos dispostos no espaço da imagem, ou seja, a posição de qualquer conteúdo na imagem caso seja alterado, de forma igual a não alterar a frequências presente na imagem,  espera-se que o resultado da transformada de fourier permaneça igual. Logo, a transformada de fourier independe da localização do objeto na imagem, caso não exista variação de intensidade entre as imagens. Contudo, se esse objeto for rotacionado em alguma angulação, essa alteração pode ser expressa na transformada de fourier. Apesar da transformada ser igual, pois independe da localização do objeto na imagem e sim das frequências, a fase da transformada de fourier sera diferente, apesar de mesma magnitude.

Na imagem abaixo, podemos ilustrar oque foi dito sobre o efeito da transformada de fourier:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q01-06.png?raw=true" alt="q01-i3-img" width="600"/>
</p>


# Questão 02

<strong>
Vimos, nos slides 16 e 17 da aula de filtragem, que o embaçamento de uma imagem provoca grandes mudanças na magnitude da transformada de Fourier dessa imagem. Considere a imagem abaixo:
</strong>

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q02-01.png?raw=true" alt="q02-i01-img" width="500"/>
</p>

<strong>
Essa imagem gera a magnitude da transformada de Fourier a seguir:
</strong>

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q02-02.png?raw=true" alt="q02-i02-img" width="500"/>
</p>

<strong>
Em comparação com a imagem da direita do slide 17, da aula de filtragem, vemos 
que o borramento parcial no canto inferior da direita, apesar de bastante forte, não 
está tão nítido na transformada. Sugira uma estratégia para detectar que houve 
esse distúrbio em alguma parte (bem definida) da imagem.
</strong>

**R.:**

## 1) **Solução 01: Gabor (1946)**

Uma apresentada em sala, é a técnica da Transformada de Fourier para Tempo Curto, ou *Short Time Fourier Transform (STFT)*, que considera uma janela que se desloca ao longo da imagem, avaliando cada momento de forma individual. Essa técnica pode ajudar a captar melhor borramentos localziamos em imagens, como ilustra a imagem abaixo:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q02-09.png?raw=true" alt="q02-i02-img" width="500"/>
</p>

Como podemos ver,  ao aplicar janelas com saltos maiores e tamanhos menores, é mais dificil de notar a região possivelmente afetada pelo ruido, contudo ao reduzirmos o tamanho da janela e o espaçamento entre elas, aumentamos o número de possibilidades para avaliação, logo tendo mais detalhes, e  facilitando a detecção da região problema.


## 2) **Solução 02: Separar em quadrantes**

Uma variação da *STFT* mencionada anteriormente, pode ser a separação direta em quadrantes a imagem, reduzindo o campo de busca para ruidos, e podendo comparar as transformadas de fourier entre elas. Em especial no exemplo da questão,  separar  em quatro quadrantes pode ser conveniente, então aplicar a transformada de Fourier em cada quadrante. Pode-se entender esta solução como um *STFT* aonde as janelas são disjuntas mas complementares para a imagem original. A ideia é que, ao analisar o espectro  individualmente para cada quadrante, será possível comparar as distribuições entre as regiões. O quadrante afetado pelo desfoque apresentará uma caracteristica diferente das outras, evidenciando o borramento.
Na imagem abaixo, da para notar a aplicação dessa solução de separação de quadrantes:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q02-08.png?raw=true" alt="q02-i02-img" width="400"/>
</p>

# Questão 03

<strong>
    Considere o filtro passa baixa de Butterworth
</strong>

$$
H(u, v) = \frac{1}{1 + \bigg[\frac{D(u, v) }{D_0}\bigg]^{2 \cdot n}}
$$

<strong>
Calcule a expressão que representa o filtro passa alta de Butterworth, a partir desse filtro passa baixa. Dicas: Observe o que foi comentado no slide 57 da aula de filtragem. Lá, é para um filtro Gaussiano, mas o raciocínio é o mesmo. O resultado final a ser calculado está no slide 65; esse é o resultado a ser alcançado. Você deve calcular como chegar nele.
</strong>

**R.:**


Sabendo que o filtro passa-alta nada mais é que o complementar do filtro passa baixa, temos então que:

$$
H_{FPA}(u, v) = 1 - H_{FPB}(u, v)
$$

Logo, substituindo a equação do filtro passa baixa de Butterworth, temos que:

$$
H_{FPA}(u, v) = 1 - \frac{1}{1 + \bigg[\frac{D(u, v)}{D_0}\bigg]^{2\cdot n}} = \frac{1 + \bigg[\frac{D(u, v)}{D_0}\bigg]^{2 \cdot n} - 1}{1 + \bigg[\frac{D(u, v)}{D_0}\bigg]^{2 \cdot n}} = \frac{\bigg[\frac{D(u, v)}{D_0}\bigg]^{2 \cdot n}}{1 + \bigg[\frac{D(u, v)}{D_0}\bigg]^{2 \cdot n}}
$$

Então,  sabendo que

$$\bigg[\frac{D(u, v)}{D_0}\bigg]^{2 \cdot n} \cdot \bigg[\frac{D(u, v)}{D_0}\bigg]^{- 2 \cdot n} = 1$$

logo:

$$
H_{FPA}(u, v) = \frac{\bigg(\frac{D(u, v)}{D_0}\bigg)^{2 \cdot n}}{\bigg(\frac{D(u, v)}{D_0}\bigg)^{2 \cdot n}   \bigg[1 + \bigg(\frac{D(u, v)}{D_0}\bigg)^{-2 \cdot n}\bigg]} = \frac{1}{1 + \bigg(\frac{D(u, v)}{D_0}\bigg)^{-2 \cdot n}}
$$

Como $$ \bigg[\frac{D(u, v)}{D_0}\bigg]^{- 2 \cdot n} =  \bigg[\frac{D_0}{D(u, v)}\bigg]^{2 \cdot n}$$

Então temos:

$$
H_{FPA}(u, v) = \frac{1}{1 + \bigg[\frac{D(u, v)}{D_0}\bigg]^{-2 \cdot n}} = \frac{1}{1 + \bigg[\frac{D_0}{D(u, v)}\bigg]^{2 \cdot n}}
$$

$$\therefore H_{FPA}(u, v) = \frac{1}{1 + \bigg[\frac{D_0}{D(u, v)}\bigg]^{2 \cdot n}} \square$$

# Questão 04

**A convolução discreta é uma operação comutativa. Ou seja:**

**f * h = h * f, onde * é a operação de convolução.**

**Comprove isso fazendo a convolução discreta dos dois filtros abaixo. Analise sua resposta.**


<div style="display: flex; align-items: center;">
  <div>
    <p>(1 / 9) * f:</p>
    <table border="1" style="border-collapse: collapse; text-align: center; margin-right: 20px;">
      <tr>
        <td>1 / 9</td>
        <td>1 / 9</td>
        <td>1 / 9</td>
      </tr>
      <tr>
        <td>1 / 9</td>
        <td>1 / 9</td>
        <td>1 / 9</td>
      </tr>
      <tr>
        <td>1 / 9</td>
        <td>1 / 9</td>
        <td>1 / 9</td>
      </tr>
    </table>
  </div>
  <div>
    <p>h:</p>
    <table border="1" style="border-collapse: collapse; text-align: center;">
      <tr>
        <td>-1</td>
        <td>0</td>
        <td>1</td>
      </tr>
      <tr>
        <td>-1</td>
        <td>0</td>
        <td>1</td>
      </tr>
      <tr>
        <td>-1</td>
        <td>0</td>
        <td>1</td>
      </tr>
    </table>
  </div>
</div>

**Ou seja, você deve calcular (e apresentar todos os cálculos) da convolução discreta das duas matrizes acima, operadas em ordens inversas: f * h e h * f.**



**R.:**

**Obs.:** Durante a questão, será marcado em **vermelho** os valores a serem somados para compor a sua localização  na matriz **m x n**.

1) <strong>Para f * h:</strong>

  Primeiramente, vamos rotacionar a segunda matriz, sendo ela **h**, ficando:

  <!-- $$
  h = \Bigg[
  \begin{array}{ccc}
  1 & 0 & -1 \\
  1 & 0 & -1 \\
  1 & 0 & -1
  \end{array}
  \Bigg]
  $$ -->


<div style="text-align: center;">
  <p>
    h: <span style="font-size: 1.5em;">
      <table style="display: inline-table; border-collapse: collapse; text-align: center;">
        <tr>
          <td>1</td>
          <td>0</td>
          <td>-1</td>
        </tr>
        <tr>
          <td>1</td>
          <td>0</td>
          <td>-1</td>
        </tr>
        <tr>
          <td>1</td>
          <td>0</td>
          <td>-1</td>
        </tr>
      </table>
    </span>
  </p>
</div>

Então, aplicando a convolução teremos:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q04-01.png?raw=true" alt="atv02-q04-01-img" width="800"/>
</p>

Logo, a matriz resultante da convolução será:

<!-- <div>
  <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML-full">
  </script>
  <p>
    $$ 
    CV^{1} = \begin{matrix}
      -0.11 & -0.11 & 0 & 0.11 & 0.11 \\
      -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
      -0.33 & -0.33 & 0 & 0.33 & 0.33 \\
      -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
      -0.11 & -0.11 & 0 & 0.11 & 0.11
    \end{matrix}
    $$
  </p>
</div> -->
<p>
  $$ 
  f * h = \left[\begin{matrix}
    -0.11 & -0.11 & 0 & 0.11 & 0.11 \\
    -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
    -0.33 & -0.33 & 0 & 0.33 & 0.33 \\
    -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
    -0.11 & -0.11 & 0 & 0.11 & 0.11
  \end{matrix}\right]
  $$
</p>


2) <strong>Para h * f:</strong>

  Primeiramente, vamos rotacionar a segunda matriz, sendo ela **f**, devido a sua natureza, a rotação dela é igual a original, logo aplicando a revolução teremos:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q04-02.png?raw=true" alt="atv02-q04-02-img" width="800"/>
</p>


Analogo ao item anterior, temos:

<p>
  $$ 
  h * f = \left[\begin{matrix}
    -0.11 & -0.11 & 0 & 0.11 & 0.11 \\
    -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
    -0.33 & -0.33 & 0 & 0.33 & 0.33 \\
    -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
    -0.11 & -0.11 & 0 & 0.11 & 0.11
  \end{matrix}\right]
  $$
</p>

3) **Conclusão:**

Logo, temos de fato que f * h = h * f.

<p>
  $$ 
  f * h = h * f = \left[\begin{matrix}
    -0.11 & -0.11 & 0 & 0.11 & 0.11 \\
    -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
    -0.33 & -0.33 & 0 & 0.33 & 0.33 \\
    -0.22 & -0.22 & 0 & 0.22 & 0.22 \\
    -0.11 & -0.11 & 0 & 0.11 & 0.11
  \end{matrix}\right] \square
  $$
</p>

# Questão 05

<strong>
Calcule uma janela para um possível filtro Gaussiano através da convolução 
discreta de três filtros Box, como abaixo: 

<p>
  $$
    \text{Filtro Box} = \left[\begin{matrix}
      1 & 1 & 1 \\
      1 & 1 & 1 \\
      1 & 1 & 1
    \end{matrix}\right]
  $$
</p>
</strong>

**R.:**

**Obs.:** Durante a questão, será marcado em **vermelho** os valores a serem somados para compor a sua localização  na matriz **m x n**. Vamos tomar como **B = Filtro Box**, para simplificar.

## 1) <strong>B * B</strong>

Calculando, devido a simetria de B, a rotação será igual, logo temos:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q05-01.png?raw=true" alt="atv02-q05-01-img" width="800"/>
</p>


Resultando em:

<p>
$$
B * B = \left[\begin{matrix}
  0.0123 & 0.0247 & 0.0370 & 0.0247 & 0.0123 \\
  0.0247 & 0.0494 & 0.0741 & 0.0494 & 0.0247 \\
  0.0370 & 0.0741 & 0.1111 & 0.0741 & 0.0370 \\
  0.0247 & 0.0494 & 0.0741 & 0.0494 & 0.0247 \\
  0.0123 & 0.0247 & 0.0370 & 0.0247 & 0.0123 \\
\end{matrix}\right]
$$
</p>


## 2) <strong>(B * B) * B</strong>

Analogo ao item anterior, devido a simetria de B, teremos rotação igual, logo temos:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q05-02.png?raw=true" alt="atv02-q05-02-img" width="800"/>
</p>

Resultado em:

<p>
$$
(B * B) * B = \left[
  \begin{matrix}
    0.0014 & 0.0041 & 0.0082 & 0.0096 & 0.0082 & 0.0041 & 0.0014 \\
    0.0041 & 0.0123 & 0.0247 & 0.0288 & 0.0247 & 0.0123 & 0.0041 \\
    0.0082 & 0.0247 & 0.0494 & 0.0576 & 0.0494 & 0.0247 & 0.0082 \\
    0.0096 & 0.0288 & 0.0576 & 0.0672 & 0.0576 & 0.0288 & 0.0096 \\
    0.0082 & 0.0247 & 0.0494 & 0.0576 & 0.0494 & 0.0247 & 0.0082 \\
    0.0041 & 0.0123 & 0.0247 & 0.0288 & 0.0247 & 0.0123 & 0.0041 \\
    0.0014 & 0.0041 & 0.0082 & 0.0096 & 0.0082 & 0.0041 & 0.0014
  \end{matrix}
\right]
$$
</p>

3) <strong>Conclusão:</strong>

Temos o produto resultante abaixo:

<p>
$$
(B * B) * B = \left[
  \begin{matrix}
    0.0014 & 0.0041 & 0.0082 & 0.0096 & 0.0082 & 0.0041 & 0.0014 \\
    0.0041 & 0.0123 & 0.0247 & 0.0288 & 0.0247 & 0.0123 & 0.0041 \\
    0.0082 & 0.0247 & 0.0494 & 0.0576 & 0.0494 & 0.0247 & 0.0082 \\
    0.0096 & 0.0288 & 0.0576 & 0.0672 & 0.0576 & 0.0288 & 0.0096 \\
    0.0082 & 0.0247 & 0.0494 & 0.0576 & 0.0494 & 0.0247 & 0.0082 \\
    0.0041 & 0.0123 & 0.0247 & 0.0288 & 0.0247 & 0.0123 & 0.0041 \\
    0.0014 & 0.0041 & 0.0082 & 0.0096 & 0.0082 & 0.0041 & 0.0014
  \end{matrix}
\right]
$$
</p>


# Questão 06

<strong>
Considere a imagem abaixo, uma imagem em 16 tons de cinza. Apresente o resultado da aplicação de um filtro Box 3x3 (o mesmo Box da questão anterior) nessa imagem. Apresente os cálculos e explique todas as decisões tomadas para realizar a filtragem, observando que sua saída deve também ser uma imagem em 16 tons de cinza.
</strong>



<div style="display: flex; align-items: center;" align="center">
  <div>
    <table border="1" style="border-collapse: collapse; text-align: center; margin-right: 20px;" align="center">
      <tr>
        <td>1</td>
        <td>3</td>
        <td>0</td>
      </tr>
      <tr>
        <td>2</td>
        <td>2</td>
        <td>3</td>
      </tr>
      <tr>
        <td>1</td>
        <td>3</td>
        <td>1</td>
      </tr>
    </table>
  </div>
</div>

**R.:**

**Obs.:** Durante a questão, será marcado em **vermelho** os valores a serem somados para compor a sua localização  na matriz **m x n**.

Como visto nas questões anteriores, a rotação da matriz de filtro box 3x3 é simétrica, então sua rotação será igual a ela mesma. 

Como visto na aula de filtragem, apartir do slide 98, vamos aplicar uma convolução entre um filtro e uma imagem, logo usaremos a **Correlação Cruzada**, definindo como estratégia para a borda será a extensão nula, e apos aplicar o processo, multiplicaremos a constante 1 / 9.

Logo:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q06-01.png?raw=true" alt="atv02-q06-01-img" width="800"/>
</p>

Então temos:

<p>
  $$
  \frac{1}{9} \cdot \text{(Img * B)} = \frac{1}{9} \cdot \left[
    \begin{matrix}
      8  & 11 & 8 \\
      12 & 16 & 12 \\
      8  & 12 & 9
    \end{matrix}
  \right] = \left[
    \begin{matrix}
      0.8889 & 1.2222 & 0.8889 \\
      1.3333 & 1.7778 & 1.3333 \\
      0.8889 & 1.3333 & 1
    \end{matrix}
    \right]
  $$
</p>

Aplicando os devidos arredondamentos, temos:

<p>
  $$
  \frac{1}{9} \cdot \text{(Img * B)} = \left[
    \begin{matrix}
      1 & 1 & 1 \\
      1 & 2 & 1 \\
      1 & 1 & 1
    \end{matrix}
    \right]
  $$
</p>

A ilustração gráfica do procedimento realizado esta abaixo:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q06-02.png?raw=true" alt="atv02-q06-02-img" width="800"/>
</p>

# Questão 07

**Disserte sobre a seguinte afirmação:**

**"As operações morfológicas de Erosão e Dilatação, aplicadas com um mesmo elemento estruturante, não são, necessariamente, operações inversas uma da outra."**

**R.:**

Enquanto a dilatação tem como objetivo expandir um objeto, a erosão visa torná-lo mais estreito. Essas operações não são necessariamente inversas, e isso pode ser exemplificado por um caso em que a erosão elimina um ponto isolado. Se uma dilatação for aplicada em seguida, esse ponto não poderá ser recuperado, uma vez que a dilatação expande apenas regiões já existentes. Se o ponto era isolado e não está mais presente na imagem, não há nada a ser expandido.

O cenário oposto também pode ocorrer: ao se aplicar uma dilatação, duas regiões próximas podem se unir. Após isso, uma erosão não será capaz de separá-las novamente, pois agora a imagem possui apenas uma única região contínua. Assim, não é possível aplicar uma suavização que recupere a separação original entre essas regiões.

Ao inves de serem tratadas como operações inversas, elas são complementares, os quais são definidos como Abertura (Suavisação de contornos em objetos, Remoção de ramos em objetos e Expansão de regiões de preto) e Fechamento (Preenchimento de falhas em regiões com contorno, diminuição de áreas de preto), a qual a primeira é a aplicação de uma erosão seguida de uma dilatação e a outra é uma dilatação seguida de uma erosão, ambas com o uso de um mesmo elemento estruturante.

# Questão 08

**Considere as imagens Book_1.png e Book_2.png disponibilizadas. Utilizando apenas técnicas de processamento de imagens, crie um algoritmo que verifique se essas imagens possuem a letra A ou não. Apenas o A maiúsculo deve ser procurado e não precisa retornar quantos têm; apenas se tem ou não. Observe que as imagens estão em preto e branco.**

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02_lista02-assets/Book_1.png?raw=true" alt="atv02-q08-01-img" width="400"/>
</p>

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02_lista02-assets/Book_2.png?raw=true" alt="atv02-q08-02-img" width="400"/>
</p>

**R.:**


Foi encontrado duas soluções possiveis para esse problema, sendo elas:

## 1) **[Lógica] Via erosão**

Essa solução apresenta uma forma mais rápida para o match, aonde é recortado da propria matriz da imagem original o bloco referente a letra de interesse (`A`) e utilizado ela como `struct` na hora de aplicar a erosão, logo será buscado na imagem original locais a qual possua esse `struct`, em caso afirmativo sera colocado branco (ou pela logica da implementação, 1) para a região encontrada do algoritmo e preto (pela logica da implementação, 0) para a região de fora do `struct`.

### 1.1) **Lógica do Algoritmo**

1. **Recorte do Objeto de Interesse**  
   Um recorte é realizado sobre a região de interesse da imagem, resultando em um template que será utilizado como struct.

2. **Binarização**  
   Binarização das imagens, tanto original quanto template.

3. **Aplicação da Erosão**  
   A operação de erosão é aplicada na imagem binarizada utilizando o template binarizado como struct.

4. **Verificação da Presença da Letra "A"**  
   Após a erosão, verifica-se se a matriz resultante contém ao menos um pixel com valor 1 (branco). Isso é feito somando os valores da matriz de erosão.


5. **Conclusão**  

  <p>
  $$
  \text{Resultado} = 
  \begin{cases} 
  \text{Letra 'A' encontrada}, & \text{se } \sum_{i = 1}^{n}\sum_{j}^{m}E_{ij} > 0 \\
  \text{Letra 'A' não encontrada}, & \text{se } \sum_{i = 1}^{n}\sum_{j}^{m}E_{ij} = 0
  \end{cases}
  $$
  </p>

Sendo:
  
<p>
  $$
  \begin{cases} 
  E, & \text{matriz de Erosão n x m}
  \end{cases}
  $$
</p>


### 1.2) **Vantagens**

Método rápido e facil de aplicar.

### 1.3) **Problema**

Necessita que o corte para a imagem de template seja o mais preciso possivel, também é ainda mais sensivel a mudança de pixels e troca de fontes. Ao invés de recortar diretamente da imagem, e sim tirar um print da letra de interesse, o método pode não funcionar, uma vez que ele busca um struct especifico de pixels alinhados.

## 2) **[Lógica] Via similaridade**

Esse método busca dar um *match* entre um template escolhido e contornos de objetos encontrados na imagem, via uma métrica pré definida e também tendo um valor de corte para essa métrica (*threshold*), com o intuito de binarizar a decisão se a imagem contem **A** ou não.

### 2.1) **Lógica do Algoritmo**

1. **Seleção do template**  
   Selecionar um template adequado, sendo o mais próximo possivel da fonte utilizada e também em dimensões.

2. **Binarização**  
   Binarização tanto da imagem original quanto do template.

3. **Busca por contornos**  
   Busca por contornos de possíveis letras ou objetos da imagem.

4. **Calculo de similaridade**  
   Calculo de similaridade entre template e contornos encontrados na imagem original. A métrica basea-se em uma correlação entre o template e a contorno de objetivo. A logica pode ser encontrada no site da [*OpenCV*](https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html),  considerando `method = TM_CCOEFF_NORMED`. A formula para essa similidade pode ser expressa pela equação abaixo:

<p>
$$
R(x, y) = \frac{\sum_{x^{'}, y^{'}} (T^{'}(x^{'}, y^{'}) \cdot I^{'}(x + x^{'}, y + y^{'}))}{\sqrt{\sum_{x^{'}, y^{'}} T^{'}(x^{'}, y^{'})^{2} \cdot \sum_{x^{'}, y^{'}} I^{'}(x + x^{'}, y + y^{'})^{2}}}
$$
</p>

Sendo:

<p>
$$
\begin{cases} 
x, y, & \text{coordenadas relativas do ponto na imagem;}\\
x^{'}, y^{'} & \text{coordenadas relativas do ponto no template;}\\
T^{'}(x^{'}, y^{'}), & \text{Valor do pixel (com T centralizado na média) no template para o ponto $(x^{'}, y^{'})$;}\\
I^{'}(x + x^{'}, y + y^{'}) & \text{Representando o pixel na imagem de entrada (com I centralizado) em uma posição deslocada}.
\end{cases}
$$
</p>

Perceba que essa métrica nada mais é do que uma correlação de pearson entre as duas variáveis, dado abaixo:

<p>
  $$
  \rho_{X, Y} = \frac{COV(X, Y)}{\sigma_{X} \cdot \sigma_{Y}} = \frac{\sum_{i=1}^{n}[(x_{i} - \bar{x})\cdot (y_{i} - \bar{y})]}{\sqrt{\sum_{i=1}^{n}(x_{i} - \bar{x})^{2}\cdot \sum_{i=1}^{n}(y_{i} - \bar{y})^{2}}}
  $$
</p>



5. **Conclusão**  
   <p>
  $$
  \text{Resultado} = 
  \begin{cases} 
  \text{Letra 'A' encontrada}, & \text{se } thres \geq 0.5 \\
  \text{Letra 'A' não encontrada}, & \text{se } thres < 0.5
  \end{cases}
  $$
  </p>


### 2.2) **Vantagens**

Método pode considerar fontes com formato proximos, dando uma flexibilidade maior ao template utilizado, podendo ter formatos um pouco diferentes de posicionamento dos pixels. Customização de métrica de similaridade entre template e imagem.

### 2.3) **Problema**

Pode ser custoso mais custoso quando lidamos com imagens maiores e com mais informações, gerando muitos contornos e tornando a busca de match exaustiva para o algoritmo.


## 3) **[Implementação] Via erosão**


### 3.0) **Leitura de imagens**

```py
image_path_1 = str(path_assets / "atv02_lista02-assets" / "Book_1.png")
image_path_2 = str(path_assets / "atv02_lista02-assets" / "Book_2.png")

image_book1 = cv2.imread(image_path_1, cv2.IMREAD_GRAYSCALE)
image_book2 = cv2.imread(image_path_2, cv2.IMREAD_GRAYSCALE)
```

### 3.1) **Definição de cortes**

Nesse momento, é feito a seleção de alguns cortes na imagem, para a seleção da letra de interesse para uso de template e `struct`. Cortes 2 e 3 são apenas ilustrativos do processo.

```py
# Configurando cortes das imagens para procura
cortes = {
    "Imagem completa": ((0, image_book1.shape[0]), (0, image_book1.shape[1])),
    "Primeiro corte": ((0, image_book1.shape[0]), (55, 87)),
    "Segundo corte": ((470, 570), (55, 87)),
    "Template final": ((501, 529), (57, 86))
}
```

Agora visualizando os cortes, temos:

```py

fig, ax = plt.subplots(1, len(cortes), figsize=(16, 12))
if not isinstance(ax, np.ndarray):
    ax = np.array([ax])
for idx, (title, sliced) in enumerate(cortes.items()):
    ax[idx].imshow(image_book1, cmap='gray')
    ax[idx].axis('off')
    if idx > 0:
        ax[idx].set_ylim(sliced[0][1], sliced[0][0])
        ax[idx].set_xlim(sliced[1][0], sliced[1][1])

    #if idx == 0:
    x_init, x_end = cortes["Template final"][1]
    y_init, y_end = cortes["Template final"][0]
    ax[idx].plot(
        [x_init] * np.ones(len(np.arange(y_init, y_end +1 ))),
        np.arange(y_init, y_end + 1),
        color='red',
        label='Média da linha'
    )

    ax[idx].plot(
        [x_end] * np.ones(len(np.arange(y_init, y_end+ 1))),
        np.arange(y_init, y_end + 1),
        color='red',
        label='Média da linha'
    )
    ax[idx].plot(
        np.arange(x_init, x_end+ 1),
        [y_init] * len(np.arange(x_init, x_end+ 1)),
        color='red',
        label='Média da linha'
    )

    ax[idx].plot(
        np.arange(x_init, x_end+ 1),
        [y_end] * len(np.arange(x_init, x_end+ 1)),
        color='red',
        label='Média da linha'
    )
    ax[idx].set_title(title)

fig.tight_layout()
fig.savefig(path_assets / "atv02-q08-s1-00.png", dpi=400, bbox_inches='tight')
plt.show()
```

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q08-s1-00.png?raw=true" alt="atv02-q08-s1-00.png" width="600"/>
</p>

Template utilizado então será:

```py
template = image_book1[
    slice(*cortes["Template final"][0]),
    slice(*cortes["Template final"][1])
]
fig, ax = plt.subplots(1, 2, figsize=(16, 10))

ax[0].imshow(
    image_book1, cmap="gray"
)
ax[0].set_title("Book_1")
ax[1].imshow(
    template,
    cmap='gray'
)
ax[1].set_title("Template retirado")
for _ax in ax:
    _ax.axis("off")

fig.savefig(path_assets / "atv02-q08-s1-01.png", dpi=400, bbox_inches='tight')
``` 

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q08-s1-01.png?raw=true" alt="atv02-q08-s1-01.png" width="600"/>
</p>


### 3.2) **Binarização**

Aqui será feita a binarização da image, para fundo preto e letra branca.

```py
# binarização
_, template_mask = cv2.threshold(template, 127, 255, cv2.THRESH_BINARY_INV)
_, image_mask_1 = cv2.threshold(image_book1, 127, 255, cv2.THRESH_BINARY_INV)
_, image_mask_2 = cv2.threshold(image_book2, 127, 255, cv2.THRESH_BINARY_INV)

# dicionario a ser usado posteriormente
imgs_mask = {
    "Book_1 - Binarizado": image_mask_1,
    "Book_2 - Binarizado": image_mask_2,
    "Template - Binarizado": template_mask
}
lista_books = list(imgs_mask.keys())[:(-1)] # seleção apenas dos books (exceto o template)

# Plot
fig, ax = plt.subplots(1, len(imgs_mask.keys()), figsize=(16, 10))
for (title, content), _ax in zip(imgs_mask.items(), ax.flatten()):
    _ax.imshow(
        content,
        cmap="gray"
    )
    _ax.set_title(title)
    _ax.axis("off")
fig.tight_layout()
fig.savefig(path_assets / "atv02-q08-s1-02.png", dpi=400, bbox_inches='tight')
plt.show()
```
<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q08-s1-02.png?raw=true" alt="atv02-q08-s1-02.png" width="600"/>
</p>

### 3.3) **Erosão**

Neste momento, vamos aplicar o processo de erosão sobre o template, que será considerado o nosso struct.

```py
# aplicar erosão morfológica usando o template como struct
eroded_results = {}
for name in lista_books:
    eroded_results[name] = {
        "eroded": cv2.erode(
            imgs_mask[name],
            template_mask,
            iterations=1
        ) / 255  # Normalizando para [0, 1]
    }
    eroded_results[name]["contains_A"] = bool(eroded_results[name]["eroded"].sum() > 0)
    eroded_results[name]["total-of_A"] = int(eroded_results[name]["eroded"].sum())
```


Para fins apenas ilustrativos, vamos dilatar o resultado dessa erosão apenas para conseguir plotar os pontos que foram encontrados de com o `struct`.


```py
# Aplicando uma dilatação apenas para visualizar melhor a localização dos A encontrados
dilated = {}
k_iter = 3
for name in lista_books:
    dilated[name] = cv2.dilate(
        eroded_results[name]["eroded"].astype(np.uint8),
        kernel=np.ones((3, 3), np.uint8), iterations=k_iter
    )

fig, ax = plt.subplots(2, 3, figsize=(22, 6))
for idx, lista in enumerate(lista_books):
    ax[idx, 0].imshow(
        imgs_mask[lista],
        cmap="gray"
    )
    ax[idx, 1].imshow(
        eroded_results[lista]["eroded"],
        cmap="gray"
    )
    ax[idx, 2].imshow(
        dilated[lista],
        cmap="gray"
    )
    for _ax in ax[idx, :]:
        _ax.axis("off")
    ax[idx, 0].set_title(lista)
    ax[idx, 1].set_title(lista.split(" - ")[0] + " - Erosão")
    ax[idx, 2].set_title(lista.split(" - ")[0] + f" - Dilatação com {k_iter} iterações")
fig.savefig(path_assets / "atv02-q08-s1-03.png", dpi=400, bbox_inches='tight')
```

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q08-s1-03.png?raw=true" alt="atv02-q08-s1-03.png" width="900"/>
</p>

Com a erosão seguida com a dilatação, considerando 3 iterações, é mais facil de visualizar graficamente a presença da letra "A".

### 3.4) **Conclusão**


```py
for key, content in eroded_results.items():
    print("-" * 30)
    print(key.split(" - ")[0])
    print(f"Possuí a letra A: {content['contains_A']}")
    if content["contains_A"]:
        print(f"Total de letra A: {content['total-of_A']}")
print("-"*30)
```
```
------------------------------
Book_1
Possuí a letra A: True
Total de letra A: 10
------------------------------
Book_2
Possuí a letra A: False
------------------------------
```

Apos a aplicação dessa solução, temos:

1) `Book_1`: a letra `A` foi detectada na imagem, além de terem sido identificados 10 letras na imagem, pela logica do algoritmo implementado no decorrer da solução.

2) `Book_2`: a letra `A` não foi detectada na imagem, pela logica do algoritmo implementado no decorrer da solução.


## 4) **[Implementação] Via similaridade**

### 4.0) **Leitura das imagens**

```py
# Leitura de imagens
file_path_template_A = str(path_assets / "atv02-q08-01_template_A.png")
image_path_1 = str(path_assets / "atv02_lista02-assets" / "Book_1.png")
image_path_2 = str(path_assets / "atv02_lista02-assets" / "Book_2.png")

image_template = cv2.imread(file_path_template_A, cv2.IMREAD_GRAYSCALE)
image_book_1 = cv2.imread(image_path_1, cv2.IMREAD_GRAYSCALE)
image_book_2 = cv2.imread(image_path_2, cv2.IMREAD_GRAYSCALE)

# parametros a serem usados ao longo da implementação
imgs = {
    "Book_1": image_book_1,
    "Book_2": image_book_2,
    "Template_A": image_template
}
books_name = ["Book_1", "Book_2"]
contents ={
    name: {
        "contornos": [],
        "letra": [],
        "letra_norm": [],
        "similarity": [],
        "check_is_valid": []
    } for name in books_name
}
```

### 4.1) **Geração de contornos**

Nesse trecho, primeiro sera feito a inversão da cor da imagem, fundo branco com letra preta, será invertido para fundo preto com letra branca, para facilitar a detecção dos contornos.

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q08-i01_k03.png?raw=true" alt="atv02-q08-i01_k03.png" width="800"/>
</p>


### 4.2) **Calculando similaridade**

Abaixo, será aplicado a cada contorno encontrado o calculo de similaridade definido na seção (`02`) dessa atividade, a qual é explicado a métrica utilizada para calcular a similaridade entre template e contorno encontrado.

```py
file_paths_imgs = {}
for name in books_name:
    fig, ax = plt.subplots(10, 10, figsize=(18, 16))
    ax = ax.flatten()
    for i, contorno in enumerate(imgs_processed[name]["contornos"]):
        x, y, w, h = cv2.boundingRect(contorno)

        letra = imgs_processed[name]["img_bin"][y:(y + h), x:(x + w)]  # recorta a letra da iamgem
        letra_resized = cv2.resize(
            letra,
            (imgs_processed["Template_A"]["img_bin"].shape[1], imgs_processed["Template_A"]["img_bin"].shape[0])
        )  # redimensiona para o tamanho do template

        letra_norm = 1 - letra_resized / 255.0 # re normalizando para retornar com o fundo branco e letra preta

        # Outro formato de uso usando a biblioteca OpenCV ###############################################################
        res = cv2.matchTemplate(
        #     letra_norm.astype(np.float32),
        #     image_template.astype(np.float32),
        #     cv2.TM_CCOEFF_NORMED
        # )[0][0]  # calculo de similaridade explicitado
        #################################################################################################################
        res = tm_ccoef_normed(letra_norm, image_template)  # calculo de similaridade
        # simililarity = res[0][0]
        simililarity = res[0][0]

        contents[name]["contornos"].append(contorno)
        contents[name]["letra"].append(letra)
        contents[name]["letra_norm"].append(letra_norm)
        contents[name]["similarity"].append(simililarity)

        if w < 10 or h < 10:  # contornos muito pequenos não serão mostrados
            if i < (10 * 10):
                ax[i].axis("off")
            contents[name]["check_is_valid"].append(False)
            continue
        contents[name]["check_is_valid"].append(True)

        if i < (10 * 10):
            ax[i].imshow(letra_norm, cmap='gray')
            ax[i].axis("off")
            ax[i].set_title(f"Sim: {simililarity:.2f}", fontsize=22)
    fig.tight_layout()
    file_paths_imgs[name] = path_assets / f"atv02-q08-i01_{name.lower()}.png"
    fig.savefig(file_paths_imgs[name], dpi=400, bbox_inches='tight')
    # fig.suptitle("Amostra de letras e similaridade calculada")
    plt.close()

# Mostra amostra de letras extraídas, juntas
fig, ax = plt.subplots(1, 2, figsize=(22, 8))
for idx, (name, file_path) in enumerate(file_paths_imgs.items()):
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    ax[idx].imshow(img, cmap = 'gray')
    ax[idx].set_title(f"Amostra de letras - {name}")
    ax[idx].axis("off")

fig.tight_layout()
fig.savefig(path_assets / "atv02-q08-i01_k04.png", dpi=400, bbox_inches='tight')
plt.show()
```

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q08-i01_k04.png?raw=true" alt="atv02-q08-i01_k04.png" width="800"/>
</p>

### 4.3) Conclusão

Considerando a regra de decisão para *match* escolhida na seção (`02`), para um `threshold` igual a `0.5`, temos o seguinte resultado:

```py
p = 0.5
file_paths_found = {}
for name in books_name:
    ks = np.where((np.array(contents[name]["similarity"]) >= p) & (np.array(contents[name]["check_is_valid"]) == True))[0]
    n = math.ceil(math.sqrt(len(ks)))
    contents[name]["contains_A"] = len(ks) > 0
    contents[name]["total-of_A"] = len(ks)
    file_paths_found[name] = path_assets / f"atv02-q08-i01_{name.lower()}_found.png"
    if n != 0:
        fig, axes = plt.subplots(
            n,
            n,
            figsize=(n * 3, n * 3)
        )


        for value, _axes in zip(ks, axes.flatten()):
            _axes.imshow(contents[name]["letra_norm"][value], cmap="gray")
            _axes.set_title(f"Contorno: {value}")

        for _axes in axes.flatten():
            _axes.axis('off')

        text = f"Letra 'A' {'encontrada' if len(ks) >= 1 else 'inexistente'}"
        text += f" | Total: {len(ks)}"
        text += f" | Imagem: {name}"
        fig.suptitle(text, fontsize=16, weight='bold')
        fig.savefig(file_paths_found[name], dpi=400, bbox_inches='tight')
        # plt.close()
    else:
        fig, axes = plt.subplots(
            1,
            1,
            figsize=(16, 8)
        )
        fig.suptitle(f"Letra 'A' não encontrada | Imagem: {name}", weight='bold')
        axes.axis('off')
        fig.savefig(file_paths_found[name], dpi=400, bbox_inches='tight')
    fig.tight_layout()
    plt.close()

# Mostra amostra de letras extraídas, juntas
fig, ax = plt.subplots(1, 2, figsize=(22, 8))
for idx, (name, file_path) in enumerate(file_paths_found.items()):
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    ax[idx].imshow(img, cmap = 'gray')
    # ax[idx].set_title(f"Amostra de letras - {name}")
    ax[idx].axis("off")

fig.tight_layout()
fig.savefig(path_assets / "atv02-q08-i01_all-found.png", dpi=400, bbox_inches='tight')
plt.show()
```

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q08-i01_all-found.png?raw=true" alt="atv02-q08-i01_all-found.png" width="800"/>
</p>

```py
for key, content in contents.items():
    print("-" * 30)
    print(key.split(" - ")[0])
    print(f"Possuí a letra A: {content['contains_A']}")
    if content["contains_A"]:
        print(f"Total de letra A: {content['total-of_A']}")
print("-"*30)
```
```
------------------------------
Book_1
Possuí a letra A: True
Total de letra A: 10
------------------------------
Book_2
Possuí a letra A: False
------------------------------
```

Apos a aplicação dessa solução, temos:

1) **Book_1:** como para a solução anterior (`01`), a letra `A` foi detectada na imagem, além de terem sido identificados 10 letras na imagem, e com esse método é possivel mensurar o quão parecidas o objeto e o template são.

2) **Book_2:** também como na solução anterior, a letra `A` não foi detectada na imagem, uma vez que consideramos o `threshold` para a similaridade de `0.5`.

# Questão 09

**Considere a imagem `cameraman_pattern.png`. Tente eliminar o padrão de linhas que aparece nela, da melhor forma possível, usando:**

**a) uma solução aplicada no domínio da frequência;**

**b) uma solução aplicada no domínio espacial.**


**R.:**

* **Obs.:** o código em notebook para essa questão pode ser encontrado clicando no [link](https://github.com/Manuelfjr/pdi/blob/develop/notebooks/04_atv02_code_q09.ipynb).

## Lendo as imagens

```py
img_names = ["cameraman.png", "cameraman_pattern.png"]
# img = cv2.imread(path_assets / "atv02_lista02-assets" / 'cameraman_pattern.png', cv2.IMREAD_GRAYSCALE)
imgs = {
    i.split(".")[0]: cv2.imread(path_imgs_atv / i, cv2.IMREAD_GRAYSCALE) for i in img_names
}
```

## Visualizando

```py
fourier = {
    name: {
        "tft": apply_fourier_transform(img)[1],
        "spectrum": apply_fourier_transform(img)[0]
    } for name, img in imgs.items()
}
# Mostrar imagem resultante
fig, ax = plt.subplots(len(fourier), 2, figsize=(16, 10))
for _ax, name in zip(ax, fourier.keys()):
    _ax[0].imshow(imgs[name], cmap='gray')
    _ax[0].set_title('Original')
    _ax[1].imshow(fourier[name]["spectrum"].astype(float), cmap='gray')
    _ax[1].set_title('Transformada de fourier')
    #_ax[0].axis('off')
    #_ax[1].axis('off')
fig.savefig(path_assets / "atv02-q09-init.png", bbox_inches='tight', dpi=400)
plt.show()

```


<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q09-init.png?raw=true" alt="atv02-q09-init-img" width="600"/>
</p>


## a)

```py
img = imgs["cameraman_pattern"]

# Aplicar a Transformada de Fourier
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

# Definir os ranges e parametros
nx = dft.shape[1]
ny = dft.shape[0]
cxrange = np.concatenate((np.arange(0, nx // 2 + 1), np.arange(-nx // 2 + 1, 0)))
cyrange = np.concatenate((np.arange(0, ny // 2 + 1), np.arange(-ny // 2 + 1, 0)))
cx, cy = np.meshgrid(cxrange, cyrange)
fxrange = cxrange * 2 * np.pi / nx
fyrange = cyrange * 2 * np.pi / ny
fx, fy = np.meshgrid(fxrange, fyrange)

# Lista de sigmas a serem procurados
sigmas = [0.3, 0.5, 0.7, 0.9, 1, 1.5, 3]

fig, ax = plt.subplots(2, (len(sigmas) // 2) + 1, figsize=(16, 10))
ax = ax.flatten()
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Original')
for _ax in ax:
    _ax.axis('off')
for idx, sigma in enumerate(sigmas):
    # Filtro passa-baixa gaussiano
    ms = np.exp(-(fx**2 + fy**2) / (2 * (sigma**2)))

    # Aplicar o filtro
    smoothF = dft * ms
    smooth = np.abs(ifft2(smoothF))

    # Exibir a imagem suavizada
    ax[idx + 1].imshow(smooth.round().astype(int), cmap='gray')
    ax[idx + 1].set_title("Filtro Passa-Baixa Gaussiano " + rf"($\sigma={sigma}$)")
    ax[idx + 1].axis('off')
fig.savefig(path_assets / "atv02-q09-a1.png", bbox_inches='tight', dpi=400)
plt.show()
```

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q09-a1.png?raw=true" alt="atv02-q09-a1" width="600"/>
</p>

### Conclusão

Analisando detalhadamente, podemos notar que os filtros considerando &sigma; = 3 e &sigma; = 0.3 podem ser descartados, uma vez que um apresentou ainda a presença do tracejado horizontal na imagem, enquanto o outro  apresenta um grau de borramento maior, quase sendo imperceptivel detectar detalhes do fundo da imagem, respectivamente.

Considerando o &sigma; = 1.5, a imagem mantem um nivel de detalhes consideravel, contudo, ainda que leve, a imagem ainda apresenta linhas tracejadas no fundo, algumas sendo bem evidentes. Os valores de &sigma; = {0.5, 0.7, 0.9} apresentaram um pouco mais de detalhes, mas um nivel de borramento ainda elevado.

Por fim, o &sigma; ideal para esse problema pode ser considerado 1, uma vez que ele conseguiu conservar detalhes da imagem, desparecendo com as linhas horizontais e ainda apresentando um nível de borramento mínimo.

## b)


Baseado na lógica do filtro box 3x3 apresentado em aula, vamos alterar um pouco a matriz h de tal forma que encontre a melhor máscara a ser aplicada. Dessa forma, vamos aplicar um conjunto de máscaras sobre a imagem, aplicando uma correlação cruzada.


```py
# mascaras utilizadas
k = 1 / 9
hs = {
    "Mascara 01": k * np.array(
        [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1]
        ]
    ),
    "Mascara 02": k * np.array(
        [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
    ),
    "Mascara 03": k * np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    ),
    "Mascara 04": k * np.array(
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
    ),
}

# aplicação da correlação cruzada
filtered_img = {
    key: convolve2d(
        imgs["cameraman_pattern"],
        h,
        mode='same',
        boundary='fill',
        fillvalue=0
    ).round().astype(int) for key, h in hs.items()
}

fig, ax = plt.subplots(2, len(filtered_img.keys()) + 1, figsize=(18, 8))

ax[0, 0].set_title('Original')
ax[0, 0].imshow(imgs["cameraman_pattern"], cmap='gray')
ax[0, 0].axis('off')

ax[1, 0].set_title('Original (sem linhas)')
ax[1, 0].imshow(imgs["cameraman"], cmap='gray')
ax[1, 0].axis('off')

# Exibir as máscaras e as imagens filtradas
for _ax, (title, content) in zip(ax.T[1:], filtered_img.items()):
    # Normalizar a máscara para  [0, 1]
    mask = hs[title]
    mask_normalized = (mask - mask.min()) / (mask.max() - mask.min())

    # _ax[0].imshow(mask_normalized, cmap='gray')
    sns.heatmap(
        mask_normalized,
        ax=_ax[0],
        cbar=False,
        annot=True,
        fmt=".0f",
        annot_kws={"color": "black", "fontsize": 12, "weight": "bold"}, 
        linewidths=0.5,
        linecolor='black',
        cmap='binary',
        vmin=1, vmax=1
    )
    _ax[0].set_title(title)
    _ax[0].axis('off')

    _ax[1].imshow(content, cmap='gray')
    _ax[1].set_title(f"Filtrado ({title})")
    _ax[1].axis('off')

fig.tight_layout()
fig.savefig(path_assets / "atv02-q09-b1.png", dpi=400, bbox_inches='tight')
plt.show()
```

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q09-b1.png?raw=true" alt="atv02-q09-b1-img" width="800"/>
</p>

### Conclusão

Entre as máscaras testadas, a Máscara 1 apresentou os melhores resultados, conseguindo remover completamente as linhas horizontais presentes na imagem cameraman_pattern.png. Além disso, essa máscara conseguiu manter os detalhes da imagem original e apresentou o menor nível de borramento.

A Máscara 2 também foi capaz de eliminar as linhas horizontais, mas apresentou um borramento mais evidente, o que comprometeu visualmente a qualidade da imagem. Por outro lado, as Máscaras 3 e 4 não foram eficazes. Ambas não foram eficientes em remover as linhas horizontais e ainda introduziram um efeito de borramento significativo, prejudicando a nitidez e os detalhes da imagem.

Dessa forma, temos que a **Máscara 1** foi a mais adequada para resolver o problema, equilibrando a remoção do padrão de linhas com a preservação da qualidade da imagem.

* **Máscara selecionada:**
<p>
$$
h = \left(\frac{1}{9}\right) \cdot \left[\begin{matrix}
    0 & 0 & 0 \\
    0 & 1 & 1 \\
    0 & 1 & 1 \\
\end{matrix}\right]
$$
</p>

# Questão 10

**Análise Escala-Espaço: Observamos o mundo ao nosso redor em diferentes escalas. Sempre temos, à nossa frente, objetos mais próximos e objetos mais distantes. Nesse sentido, tomando como base a teoria de Marr, Pietro Perona e Jitendra Malik propuseram um método de detecção de bordas, usando a teoria escala-espaço. A ideia principal é que, em diferentes escalas da imagem, diferentes bordas se sobressaem. Essa variação de escala poderia ser conseguida com a aplicação de sucessivos resizes na imagem. No entanto, como cada resize tem como consequência, além da mudança de dimensões de uma imagem, a perda de detalhes, essa operação foi substituída pela aplicação de filtros Gaussianos de diferentes parâmetros. À medida que o filtro se torna mais forte (maior o desvio padrão), mais embaçada a imagem fica o que gera a perda de detalhes esperada.**

**Comprove a aplicação da teoria escala-espaço na detecção de bordas com o seguinte experimento: na imagem cameraman.png, aplique três filtros gaussianos diferentes (parte de um mais fraco e vá até um mais forte), detecte as bordas de cada um com o detector de Canny (precisa usar os mesmos parâmetros para todas as imagens) e, por fim, avalie os resultados finais, verificando se diferentes bordas foram encontradas.**

**OBS: Não se preocupe em achar um resultado final de boa qualidade; não é esse o objetivo do experimento**

**R.:**

* **Obs.:** o código em notebook para essa questão pode ser encontrado clicando no [link](https://github.com/Manuelfjr/pdi/blob/develop/notebooks/04_atv02_code_q10.ipynb).

O intuito desse experimento é verificar a detecção das bordas apos a aplicação de três filtros gaussianos, e analisar o contorno encontrado apos cada filtro. Dessa forma, o esperado é que o nível de detalhe caia, a medida que se aumenta o sigma do filtro gaussiano, causando um efeito de perca de detalhes.

* **Leitura**

```py
img_names = ["cameraman.png"]
imgs = {
    i.split(".")[0]: cv2.imread(path_imgs_atv / i, cv2.IMREAD_GRAYSCALE) for i in img_names
}
```

* **Configurando parâmetros**

```py
# Sigmas para o filtro gaussiano
sigmas = [1, 2, 4]

# Parametros para o método de deteccao de canny
low = 50
high = 150
```

* **Implementação e geração de gráficos**

```py
fig, ax = plt.subplots(1, len(sigmas), figsize=(16, 8))
ax = ax.flatten()
for i, sigma in enumerate(sigmas):
    # Aplica filtro Gaussiano com sigma definido
    blurred = cv2.GaussianBlur(
        imgs["cameraman"],
        (0, 0),
        sigmaX=sigma,
        sigmaY=sigma
    )

    # Detecta bordas com Canny
    edges = cv2.Canny(
        blurred,
        low,
        high
    )

    # Exibe os resultados
    ax[i].imshow(edges, cmap='gray')
    ax[i].set_title(f'Canny{low, high} | Filtro gaussiano:' + rf'$\sigma$={sigma}')
    ax[i].axis('off')
fig.tight_layout()
fig.savefig(path_assets / "atv02-q10-02.png", dpi=400, bbox_inches='tight')
plt.show()
```

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q10-02.png?raw=true" alt="atv02-q10-02-img" width="800"/>
</p>

* **&sigma; = 1**: existe diversas bordas, mostrando um nivel de detalhe bem significante, preservando pontos princiapis da imagem e secundários também. Isso se da possivelmente pelo valor de &sigma; baixo, causando um efeito de emabaçamento menor. 

* **&sigma; = 2**: destaque nos detalhes principais, sumindo parcialmente traços mais secundários como os da grama. O filtro Gaussiano mais forte suaviza regiões pequenas, e o detector de bordas começa  a destacar contornos mais marcantes.

* **&sigma; = 4**: apenas as bordas principais da imagem são visíveis. Com o aumento da suavização, diversos detalhes desaparecem, restando apenas as transições de contraste mais evidentes.

Essa progressão demonstra que, ao aumentar o valor de &sigma; no filtro Gaussiano, esta focando na imagem apenas os pontos mais caracteristicos, ou seja, apenas bordas maiores e mais importantes são conservadas. Dessa forma, diferentes bordas aparecem em diferentes escalas, demonstrando a ideia da análise escala-espaço como uma ferramenta bem interessante na segmentação  de imagens com muitos objetos visuais.