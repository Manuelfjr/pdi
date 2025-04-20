<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML-full">
</script>


# Atividade 02

* **Aluno:** Manuel Ferreira Junior
* **Disciplina:** Processamento Digital de Imagens

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
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q01-05.png?raw=true" alt="q01-i3-img" width="600"/>
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

<strong>
A convolução discreta é uma operação comutativa. Ou seja:

f * h = h * f, onde * é a operação de convolução.

Comprove isso fazendo a convolução discreta dos dois filtros abaixo. Analise sua resposta.


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

Ou seja, você deve calcular (e apresentar todos os cálculos) da convolução discreta 
das duas matrizes acima, operadas em ordens inversas: f * h e h * f.
</strong>


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
    h = 
    <span style="font-size: 1.5em;">
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

2) <strong>Para h * f:</strong>

  Primeiramente, vamos rotacionar a segunda matriz, sendo ela **f**, devido a sua natureza, a rotação dela é igual a original, logo aplicando a revolução teremos:

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv02-q04-02.png?raw=true" alt="atv02-q04-02-img" width="800"/>
</p>


# Questão 05

<strong>
5. Calcule uma janela para um possível filtro Gaussiano através da convolução 
discreta de três filtros Box, como abaixo: 
Filtro Box = 
</strong>