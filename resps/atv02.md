<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML-full">
</script>

# Atividade 02

* **Aluno:** Manuel Ferreira Junior
* **Disciplina:** Processamento Digital de Imagens

* **Obs.:** Questões com necessidade de calculo de convolução, estarão todas as expressões no [link](https://docs.google.com/spreadsheets/d/1cWB3zNBbDXzFNvEKotBCVPIlnS8cde-SXRjCP55ISTM/edit?usp=sharing), para facilitar a visualização e leitura da atividade. Além disso, cada questão em anexo possui uma copia da sua operação que deve ser realizada. Cada sheet do link em anexo, possui no seu titulo a questão referente e operação referente.

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

A Transformada de Fourier tem como foco principal analisar a distribuicao das frequências da iamgem e não elementos dispostos no espaço da imagem, ou seja, a posição de qualquer conteúdo na imagem caso seja alterado, de forma igual a não alterar a frequências presente na imagem,  espera-se que o resultado da transformada de fourier permaneça igual. Logo, a transformada de fourier independe da localização dos pixels sobre a imagem, caso não exista variação de intensidade entre as imagens.

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


Uma possivel estrategia para detectar esse tipo de anomalia localizada, como  o borramento em regiões especificas, pode ser segmentar a imagem em regiões menores, em especial no exemplo da questão, em quatro quadrantes, ai então aplicar a transformada de Fourier em cada quadrante. A ideia é que, ao analisar o espectro  individualmente para cada quadrante, será possível comparar as distribuições entre as regiões. O quadrante afetado pelo desfoque apresentará uma caracteristica diferente das outras, evidenciando o borramento.


Na imagem abaixo, da para ntoar a aplicação dessa solução de separação de quadrantes:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q02-07.png?raw=true" alt="q02-i07-img" width="500"/>
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


Ilustrando graficamente o efeito desse filtro box, temos:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q05-03.png?raw=true" alt="atv02-q05-03-img" width="800"/>
</p>

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q05-04.png?raw=true" alt="atv02-q05-04-img" width="800"/>
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