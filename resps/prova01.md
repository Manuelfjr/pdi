<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML-full">
</script>

# Prova 01

* **Aluno:** Manuel Ferreira Junior
* **Matricula:** 20241032637
* **Disciplina:** Processamento Digital de Imagens

# Questão 01

Como dado na questão, ambas as imagens estão em uma mesma resolução, então podemos afirmar que, supondo que a região preta trata-se de objetos iguais, podemos notar que na segunda imagem, o objeto sofreu uma consideravel rotação. Como visto em sala, ao aplicarmos a transformada de fourier da imagem com um objeto claro como na primeira imagem, aonde temos um cenário binario para facilitar (preto e branco), ela ira apresentar um comportamento esperado e se rotacionarmos apenas o objeto, mantendo o mesmo comportamento, espera-se que a transformada de fourier que originalmente teria um comportamento similarar a uma cruz, aonde sobre a cruz estariam os valores maiores e fora menores, sendo o  centro de maior pico, com a rotação espera-se que apareça mais traços com picos, em uma angulação exata ao que foi rotacionado na imagem.

obs.: a solução proposta propoe que o objeto possui mesmo tamanho.

Dessa forma, podemos definir o seguinte algoritmo:

1) Fixar um template de imagem sem rotação (como na primeira imagem)

2) Extrair a transformada de fourier da segunda imagem

3) aplicar uma equação representando um erro, como um calculo de distancia da transformada de fourier no template e a trnasformada obtida da segunda imagem, aonde temos algo como:

<p>
$$
ERRO = d(T, \hat{T}) =  \sum_{i = 1}^{n}\sum_{j = 1}^{n} | t_{ij} - \hat{t}_{ij} |
$$
</p>

sendo 

<p>
$$
T = {t_{ij}}_{m x n}
$$
</p>

e

<p>
$$
\hat{T} = \{\hat{t}_{ij}\}_{m x n}
$$
</p>

4) apartir disso, vamos poder checar se houve alguma mudança no posicionamento do objeto para captação da imagem, evidenciando principalmente situações de rotações, uma vez que a transformada de fourier é sensivel a esse tipo de situação. Dessa forma, para garatir a deteção de leves rotações, podemos considerar um threshold como um erro superior a um ponte de corte, por exemplo, de `ERRO > 2` (ou algum threshold definido empiramente) será emitido um alerta para o `operador` que o objeto esta rotacionado. Este cálculo auxilia também para detecção de redução do objeto na imagem, uma vez que considera mesma resolução e todos os valores obtidos da matriz resultante da operação da transformada de fourier

5) Para checagem da redução diretamente, podemos apenas pegar o pico central obtido na matriz de fourier, e comparar diretamente com a obtida do template, calculando a diferença absoluta, se a diferença também for maior que um erro como `ERRO_REDUCAO > 2` (ou algum threshold definido empiramente), podemos definir que houve alguma redução da imagem.

6) Por fim, em caso de Verdadeiro os items (4) e (5), temos que houve uma rotação e uma redução da imagem.

# Questão 02

Com a aplicação da transformada de fourier nessa imagem de 256 tons de cinza, esperava-se uma uma imagem da magnitude com  suas altas frequências bem definidas, mas aparenemte essa imagem possui algum tipo de ruido, bem parecido com ruido de borramento na imagem sobre a imagem.

# Questão 03

## A)

Vamos converter em mascaras d diretamente para cada equação, sendo então:

1) para Eq. (1), com a equação:

<p>
$$
\frac{\partial^2 f}{\partial x^2} \approx f(x - 1, y) - 2f(x, y) + f(x + 1, y)
$$
</p>

temos: 

</p>
$$
h_{y} = \left[\begin{matrix}
0 & 0 & 0\\
1 & -2 & 1 \\
0 & 0 & 0
\end{matrix}\right]
$$
</p>

2) para Eq. (1), com a equação:

<p>
$$
\frac{\partial^2 f}{\partial y^2} \approx f(x, y - 1) - 2f(x, y) + f(x, y + 1)
$$
</p>

temos: 

</p>
$$
h_{y} = \left[\begin{matrix}
0 & 1 & 0\\
0 & -2 & 0 \\
0 & 1 & 0
\end{matrix}\right]
$$
</p>

logo temos as mascaras, de menor ordem possivel.

## B)

Aplicando a convolução entre h<sub>x</sub> e h<sub>y</sub>, uma vez que a ambas são simetricas, torna-se mais facil o calculo. Em anexo os calculos.

# Questão 04

Como temos um filtro e uma imagem, vamos aplicar uma correlação cruzada para a convolução. Sendo f a imagem e h o filtro, temos que o filtro é simetrico, então a rotação sera igual a propria matriz. **Resultado anexado**.


Além da resolucao em anexo, foi feito o processo realizado como na figura abaixo ou clicando no [link](https://docs.google.com/spreadsheets/d/12o_qU6SxuKznBXWL_qrwQOmXumow0_PUY-tVPeBAhng/edit?usp=sharing). Para cada posição, o calculo se da baseado na soma de todos os valores na cor vermelha.

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/q04_prova01.png?raw=true" alt="q01-i2-img" width="600"/>
</p>



# Questão 05

Como visto nas aulas de morfologia matemática, podemos aplicar um elemento estruturante em uma **operação de erosão**, considerando um template especifico, para a checagem se esse elemento estruturante esta presente na imagem. Para isso, vamos aplicar a erosão com dois elemento estruturantes diferentes ("B" e "F"), de forma separadas na imagem, considerando os templates obtidos apartir da propria matriz da imagem.


0) **Leitura da imagem:** lendo a imagem para aplicação do processamento;

1) **Obtenção dos templates para B e F:** localização dos templates dentro da propria imagem para as letras B e F;

2) **Aplicação do processo de erosão com os elemento estruturantes:** aplicação do processo de erosão, de forma individual para cada elemento estruturante sobre a imagem.

3) **Para cada matriz obtida, checamos se o elemento estruturante foi encontrado:** em cada matriz individual, B e F, checamos se com o processo de erosão a matriz resultante apresenta ao menos um valor maior que zero, **para ambas as letras**, então a imagem possui as letras B e F nela.

Em suma, temos:

<p>
$$
\text{Resultado} = 
\begin{cases} 
\text{Letra 'B' e 'F' encontrada}, & \text{se } \sum_{i = 1}^{n}\sum_{j = 1}^{m}e^{('B')}_{ij} > 0 \text{ e } \sum_{i = 1}^{n}\sum_{j = 1}^{m}e^{('F')}_{ij} > 0 \\
\text{Letra 'B' e 'F' não encontrada}, & \text{se } \sum_{i = 1}^{n}\sum_{j = 1}^{m}e^{('B')}_{ij} = 0 \text{ e } \sum_{i = 1}^{n}\sum_{j = 1}^{m}e^{('F')}_{ij} = 0
\end{cases}
$$
</p>


sendo 

<p>
$$
E^{('B')} = \{e^{'B'}\}_{mxn}
$$
</p>

e

<p>
$$
E^{('F')} = \{e^{'F'}\}_{mxn}
$$
</p>