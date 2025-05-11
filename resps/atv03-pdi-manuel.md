<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML-full">
</script>

# Atividade 03

* **Aluno:** Manuel Ferreira Junior
* **Disciplina:** Processamento Digital de Imagens


# Questão 01
<strong>
Para esta questão, considere as imagens: 

Pattern1.png 

Pattern1_blur.png 

Pattern1_blur2.png 

Pattern2.png 

As imagens Pattern1_blur e Pattern1_blur2 são versões embaçadas com diferentes 
intensidades da imagem Pattern1. 
</strong>

## A)

**Nas imagens Pattern1 e Pattern2, calcule a magnitude da Transformada de Fourier e disserte sobre esse gráfico em relação às imagens originais, observando o que acontece com as altas e baixas frequências.**

Como pode ser visto na questão, a transformada de fourer é uma ferramente essencial para analise da frequência dos contrastes na imagem, podendo ajudar a identificar padrões espaciais distribuidos ao longo da imagem original, apartir de analises de altas e baixas frequências. Nesse caso, para as imagens *Pattern1* e *Pattern2*, é possivel observar dois comportamentos bem distintos como visto abaixo

<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv03_q01-01.png?raw=true" alt="q01-i1-img" width="600"/>
</p>

A imagem *Pattern1* apresenta um padrão periodo, sendo ele definido por traçados diagonais  bem definidos e continuos, indicando uma periodicidade na estrutura da imagem, sendo evidenciado ainda mais ao analisar a FFT da imagem, com picos localizados e simétricos. O padrão regular encontrado na transformada de fourier evidencia o comportamento periodico da imagem original, devido a essa presença de picos e simetrias na magnitude da transformada.

A segunda imagem, *Pattern2*, possui um padrão mais desordenado, comparado a primeira imagem, não tendo um comportamento periodico completo e sim mais complexo. Contudo a imagem ainda que sem periodicidade completa, existe partes da imagem que apresentam alguma periodicidade mesmo que em pouco espaço. Aparentemente, existem uma interseção entre dois comportamentos, um horizontal e outro diagonal na imagem, isso se reflete na transformada de fourier, tendo uma distribuição mais espalhada, contudo com uma região circular no centro, com alguns picos ao longo do perimetro da circunferencia. Uma diferença clara entre as transformadas, que pode ser evidenciada mais claramente quando olhamos o plot 3D das transformadas, é a presença de 2 picos bem evidentes na primeira imagem *Pattern1*, enquanto a *Pattern2* apresenta alguns picos proximos dentro da circunferencia central.

Comparando ambas as imagens e suas transformadas, podemos notar que uma imagem com um comportamento periodico claro, ao longo da imagem completa (*Pattern1*) apresenta uma representação na magnitude da transformada de fourier bem definida, com traços simetricos e com picos bem definidos; Já imagens com padrão tão complexos, como a sobreposição de comportamentos horizontais e diagonais, além da alteração da frequência dos tons, devem apresentar uma transformada com um comportamento mais complexos, como no exemplo, uma circunferencia com raio bem definido, e diversos picos ao longo do centro.


## B)

**Agora, analise o que acontece com a magnitude da Transformada de Fourier à medida que filtros passa baixa vão sendo aplicados na imagem Pattern1 com intensidades cada vez mais fortes. Isso pode ser visto nas imagens Pattern_blur e Pattern_blur2; não é necessário embaçar mais a imagem original.**


<p align="center" >
    <img src="https://github.com/Manuelfjr/pdi/blob/develop/assets/atv03_q01-02.png?raw=true" alt="q01-i2-img" width="600"/>
</p>


# Questão 04