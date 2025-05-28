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

**R.:**

Como pode ser visto na questão, a transformada de fourer é uma ferramente essencial para analise da frequência dos contrastes na imagem, podendo ajudar a identificar padrões espaciais distribuidos ao longo da imagem original, apartir de analises de altas e baixas frequências. Nesse caso, para as imagens *Pattern1* e *Pattern2*, é possivel observar dois comportamentos bem distintos como visto abaixo

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q01-01.png" alt="q01-i1-img" width="600"/>
</p>

A imagem *Pattern1* apresenta um padrão periodo, sendo ele definido por traçados diagonais  bem definidos e continuos, indicando uma periodicidade na estrutura da imagem, sendo evidenciado ainda mais ao analisar a FFT da imagem, com picos localizados e simétricos. O padrão regular encontrado na transformada de fourier evidencia o comportamento periodico da imagem original, devido a essa presença de picos e simetrias na magnitude da transformada.

A segunda imagem, *Pattern2*, possui um padrão mais desordenado, comparado a primeira imagem, não tendo um comportamento periodico completo e sim mais complexo. Contudo a imagem ainda que sem periodicidade completa, existe partes da imagem que apresentam alguma periodicidade mesmo que em pouco espaço. Aparentemente, existem uma interseção entre dois comportamentos, um horizontal e outro diagonal na imagem, isso se reflete na transformada de fourier, tendo uma distribuição mais espalhada, contudo com uma região circular no centro, com alguns picos ao longo do perimetro da circunferencia. Uma diferença clara entre as transformadas, que pode ser evidenciada mais claramente quando olhamos o plot 3D das transformadas, é a presença de 2 picos bem evidentes na primeira imagem *Pattern1*, enquanto a *Pattern2* apresenta alguns picos proximos dentro da circunferencia central.

Comparando ambas as imagens e suas transformadas, podemos notar que uma imagem com um comportamento periodico claro, ao longo da imagem completa (*Pattern1*) apresenta uma representação na magnitude da transformada de fourier bem definida, com traços simetricos e com picos bem definidos; Já imagens com padrão tão complexos, como a sobreposição de comportamentos horizontais e diagonais, além da alteração da frequência dos tons, devem apresentar uma transformada com um comportamento mais complexos, como no exemplo, uma circunferencia com raio bem definido, e diversos picos ao longo do centro.


## B)

**Agora, analise o que acontece com a magnitude da Transformada de Fourier à medida que filtros passa baixa vão sendo aplicados na imagem Pattern1 com intensidades cada vez mais fortes. Isso pode ser visto nas imagens Pattern_blur e Pattern_blur2; não é necessário embaçar mais a imagem original.**


<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q01-02.png" alt="q01-i2-img" width="600"/>
</p>

**R.:**


Logo apos a primeira aplicação do filtro passa baixa, a imagem já tem seu ruido periodico retirado, os traços horizontais ao longo da imagem desparecem e ocorre o efeito de borramento esperado apos aplicação do filtro. Analisando a transformada de fourier, é mais nitido a cruz horizontal e vertical na magnitude bem definida, porém algumas altas frequências aparentam estar espalhadas ainda ao longo da matriz de transformada. Um ponto interessante de se ressaltar, é o desaparecimento dos picos de alta frequência anteriores, agora restando apenas um pico de alta frequência, com alguns outros picos espalhados mas maioria centrado ao longo da cruz. Apos aplicação do segundo filtro passa baixa, a cruza permanece ainda com altas frequência, mas ainda sim bem reduzidos comparado a primeira aplicação do filtro, e o comportamento das altas frequências espalhadas agoram se encontram mais proxima do centro, ou seja, mais eprto do pico de alta frequência da imagem.


# Questão 02

<strong>
Para esta questão, considere a imagem XRay.png. 
Três ações são necessárias para esse tipo de aplicação: 

a) Detectar a mão; 

b) Detectar os ossos; 

c) Detectar o anel. 

Os resultados esperados (aproximados) podem ser vistos nas figuras abaixo: 
</strong>


<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03-q02-00.png" alt="atv03-q02-00" width="600"/>
</p>

<strong>
Reforço que as imagens acima são resultados aproximados apenas. Desenvolva algoritmo(s) que resolvam os problemas acima de <u>forma automática</u>, com as 
técnicas vistas na disciplina. Pode ser um algoritmo apenas que sirva para os três casos, pode ser um algoritmo para cada caso, mas tem que ser automático e tem que usar apenas técnicas vistas na disciplina (ou manipulação matemática comum para matrizes).
</strong>

**R.:**

Obs.: Os três procedimentos possuem formas de busca distintas.

## **1) Mão**

* **1) Leitura da imagem:** A imagem "XRay.png" é lida em escala de cinza e ajustada para remover as duas primeiras colunas.

```py
# Leitura
file_path_img = "XRay.png"
img = cv2.imread(path_imgs_atv / "Q2" / file_path_img, cv2.IMREAD_GRAYSCALE)
img = img[:, 2:]  # exclusão do bug de duas colunas de pixel branca na imagem
```

* **2) Quantização dos tons de cinza:** A imagem é quantizada em 4 níveis de intensidade usando os quartis dos valores de pixel. Cada pixel é substituído pelo valor médio do intervalo ao qual pertence, reduzindo a quantidade de tons e agrupando regiões semelhantes. Essa técnica se assemelha a usada na questão 03. Dado os 4 níveis, teremos o seguinte:

dada a imagem:

<p>
$$
Img = \left[\begin{matrix}
    pixel_{00} & pixel_{01} & \dots & pixel_{0m} \\
    pixel_{10} & pixel_{11} & \dots & pixel_{1m} \\
    \vdots & \vdots & \ddots & \vdots \\
    pixel_{n0} & pixel_{n1} & \dots & pixel_{nm} \\
\end{matrix}\right]
$$
</p>

e que, como dividimos em 4 niveis, temos os valores [0, 0.25, 0.5, 0.75], ou seja, calculando o ponto médio de cada intervalo, temos:

<p>
$$
\begin{cases}
    \frac{q_{0\%} + q_{25\%}}{2} & \text{ se } q_{0\%} \leq pixel_{ij} \leq q_{25\%}; \\
    \frac{q_{25\%} + q_{50\%}}{2} & \text{ se } q_{25\%} \leq pixel_{ij} \leq q_{50\%}; \\
    \frac{q_{50\%} + q_{75\%}}{2} & \text{ se } q_{50\%} \leq pixel_{ij} \leq q_{75\%}. \\
\end{cases}
$$
</p>

com "i" variando na linha e "j" na coluna da matriz da imagem, sendo feita uma checagem ao longo da imagem para cada pixel, agrupando as cores pertencentes a aquele range. Abaixo temos o codigo:

```py
# agrupamento de tons
img_test = img.copy()
k_bins = 4  # número de faixas a ser procurada.
quantils = np.arange(0, 1, 1 / k_bins)  # quantis [0, 0.25, 0.50, 0.75]
img_quantiles = np.quantile(img_test, quantils)
values = ((img_quantiles[1:] + img_quantiles[:-1]) / 2).astype(int)  # calculo do valor a ser substituido.
for row in range(img_test.shape[0]):
    for col in range(img_test.shape[1]):
        idx = np.digitize(img_test[row, col], img_quantiles) - 1
        idx = np.clip(idx, 0, len(values) - 1)
        img_test[row, col] = values[idx]
```

* **3) Binarização (Otsu):** A imagem quantizada é binarizada automaticamente pelo método de Otsu, separando regiões claras e escuras.

```py
img_bin = cv2.threshold(img_test, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
```

* **4) Fechamento morfológico:** Um fechamento morfológico é aplicado para remover pequenos buracos e ruídos na máscara binária.

```py
kernel = np.ones((5, 5), np.uint8)
img_close = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel, iterations=1)
```

* **5) Suavização (Gaussian Blur):** Um filtro Gaussiano é aplicado para suavizar a máscara, tornando as bordas menos abruptas.

```py
img_gaussian = cv2.GaussianBlur(img_close, (3, 3), 1)
```

* **6) Sobreposição da máscara na imagem original:** A máscara resultante é sobreposta na imagem original convertida para RGB, colorindo de azul as regiões detectadas.

```py
img_rec = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
img_rec[img_gaussian > 0] = [0, 0, 255]  # Azul
```

* **7) Conclusão:** Todas as etapas intermediárias e finais são armazenadas em um dicionário para facilitar a visualização e comparação dos resultados. Abaixo, é ilustrado os procedimentos anteriores em sequência.

```py
imgs_mao = {
    (0, 0): {"img": img_color, "title": "1) Imagem original"},
    (0, 1): {"img": img_test, "title": "2) Quantização (Agrupamento de tons)"},
    (0, 2): {"img": img_bin, "title": "3) Binarização (Otsu)"},
    (1, 0): {"img": img_close, "title": "4) Fechamento morfológico"},
    (1, 1): {"img": img_gaussian, "title": "5) Suavização (Gaussian Blur)"},
    (1, 2): {"img": img_rec, "title": "6) Imagem final"}
}

# Plotando as imagens usando o dicionário
rows, cols = 2, 3
fig, ax = plt.subplots(rows, cols, figsize=(16, 10))
for (i, j), data in imgs_mao.items():
    ax[i, j].imshow(data["img"], cmap='gray')
    ax[i, j].set_title(data["title"])
    ax[i, j].axis('off')

# Esconde os subplots não usados
for _ax in ax.flatten():
    _ax.axis('off')

fig.tight_layout()
fig.savefig(path_assets / "atv03_q02-01.png", dpi=400)
plt.show()
```

Podemos ver que o método desenvolvido conseguiu demarcar bem a região da mão, tendo dificuldade na região do menor dedo e o anelar. O procedimento mostrou efetivo para a imagem, conseguindo mapear todo o contorno da mão.

## **2) Ossos**



# Questão 03

<strong>Nas imagens coloridas da questão, implemente um algoritmo automático que diminua a quantidade de cores das imagens, agrupando tons semelhantes (por exemplo, uma região de tons avermelhados deve ser tornar uma região com apenas um tom de vermelho). Não deve ser usado dithering. Considere que a imagem final pode ter, aproximadamente, de metade a um terço da quantidade de cores das imagens originais. Cada imagem tem: 
</strong>

* **araras.png**: 112.233 cores;  
* **F1.png**: 85.837 cores;  
* **green-water.png**: 33.801 cores;  
* **surf.png**: 47.229 cores. 

**O mesmo algoritmo deve ser usado nas 4 imagens. Observações:**

1) **Se precisar, pode usar conversões entre modelos de cores já implementadas em Python ou qualquer outra linguagem.**

2) **Não pode usar K-means ou  qualquer outra técnica de agrupamento.**

3) **Só pode usar técnicas vistas na disciplina.**

4) **Todo o processo deve ser automático sem participação do usuário.**

**R.:**

O algoritmo ira se basear em agrupar cores proximas, considerando faixas de bins  definidas entre 0 e 255 para cada canal de cor. Se o valor daquele pixel pertencer a esse intervalo, ele sera atribuido o ponto médio do intervalo.

O algoritmo ira realizar uma busca exaustiva entre um numero "a" de bins a um numero "b" de bins, com salto definido como "p". O intuito dessa busca exaustiva é tentar achar o número de bins ideal para que seja satisfeita a condição de que o número total de cores da imagem esteja entre 1 / 3 a 50% do total de cores da imagem original.

Vamos definir por partes, primeiro a logica da implementação, e em seguida a implementação utilizando o python.

## [Algoritmo] Apoximação por bins

1) **Definir condições de busca:**

    * **Quantidade de bins:** para cada canal, será feito uma quebra em bins (ex.: 0 a 63, 64 a 127, 128 a 191 e 192 a 255, total de 1 bin com 5 faixas). Nesse passo, será definido uma lista de possiveis bins para busca, por exemplo, se selecionar 50 a 150 com salto de 10, teremos o primeiro bin que ira quebrar o intervalo de 0 a 255 em 50 partes de tamanho igual, o segundo bin irá quebrar o intervalo de 0 a 255 em 60 partes, o terceiro bin irá quebrar o intervalo de 0 a 255 em 70 partes, e assim por diante, até chegar no bin que dividirá em 150 partes; na parametrização da solução vamos considerar o inicio igual a 50, e o final da procura em 150 bins, considerando um salto de 10.

    * **Parâmetros usados:**
        
        Abaixo temos descrito quais parametros de range de busca foram utilizados.

        * `inicio (a)`: 50
        
        * `final (b)`: 150

        * `salto (step)`: 10

2) **Definição de critério de parada:**

    * **Critério de parada:** para cada iteração de bins do passo **(1)**, será realizado uma checagem de parada, aonde a condição será definida por:

    <p>
    $$
    \begin{cases} 
    \text{Parar busca e seleção do i-ésimo bin }  ( B = b^{(i)}), & \text{se } \frac{1}{3}\cdot T_{o} \leq T^{(i)}_{r} \leq 0.5 \cdot T_{o}\\
    \text{Próxima iteração}, & \text{se } T^{(i)}_{r} < \frac{1}{3} \cdot T_{o} \text{ ou }  T^{(i)}_{r} > 0.5 \cdot T_{o} 
    \end{cases}
    $$
    </p>

    Sendo:

    <p>
    $$
    \begin{cases}
    T^{(i)}_{r}: &  \text{Total de cores da imagem para o } \text{ i - ésimo bin} \\
    T_{o}: & \text{Total de cores da imagem original}
    \end{cases}
    $$
    </p>

    Além da checagem para convergência acima para cada iteração, em um caso de não satisfazer a condição definida para nenhum bin, será atribuido aquele que minimize o número de cores, ou seja:

    <p>
    $$
    B = min_{a \leq i \leq b, step}\{ b^{(i)} \}
    $$
    </p>

    Sendo:

    <p>
    $$
    \begin{cases}
    B: \text{ Bin escolhido ao longo das iterações} \\
    b^{(i)}: \text{ i-ésimo bin a ser usado} \\
    a: \text{ Número inicial de bins para procura} \\
    b: \text{ Número final de bins para procura} \\
    step: \text{ Salto a ser dado a cada iteração de um bin para o próximo}
    \end{cases}
    $$
    </p>

3) **Processo de calculo para redução:**
    
    **Obs.:** O processo a ser descrito será aplicado para cada canal existente.
    
    **Definição:** Para cada iteração, o i-ésimo bin, será gerado faixas baseado na média entre `bin[1:]` e `bin[:(-1)]`, ou seja:

    <p>
    $$
    b^{(i)} = [x_{0}, x_{1}, \dots, x_{n}]
    $$
    </p>

    aonde o novo valor a ser atribuido para cada pixel será definida pelas entradas do vetor abaixo:

    <p>
    $$
    \text{V} = \frac{\left[\begin{matrix}
    x_{1} \\
    x_{2} \\
    \vdots \\
    x_{n}
    \end{matrix}\right] + \left[\begin{matrix}
    x_{0} \\
    x_{1} \\
    \vdots \\
    x_{n - 1}
    \end{matrix}\right]}{2} = \frac{
        \left[
            \begin{matrix}
            x_1 + x_0 \\
            x_2 + x_1 \\
            \vdots \\
            x_n + x_{n - 1}
            \end{matrix}
        \right]
    }{2} = \left[
        \begin{matrix}
        \frac{x_1 + x_0}{2} \\
        \frac{x_2 + x_1}{2} \\
        \vdots \\
        \frac{x_n + x_{n - 1}}{2}
        \end{matrix}
    \right]
    $$
    </p>

    Logo, para cada valor novo por pixel para cada canal, teremos a atribuição abaixo:

    <p>
    $$
    \begin{cases}
    \frac{x_1 + x_0}{2}, &  \text{ se }  x_0 \leq pixel_{00} \leq x_1 \\
    \frac{x_2 + x_1}{2}, &  \text{ se }  x_1 \leq pixel_{00} \leq x_2 \\
    \vdots \\
    \frac{x_{n} + x_{n - 1}}{2}, &  \text{ se }  x_{n - 1} \leq pixel_{00} \leq x_{n}
    \end{cases}
    $$
    </p>

    Isso será feito para cada canal da imagem (Img), pixel a pixel, ou seja, aplicado para cada canal na sua respectiva matriz abaixo:

    <p>
    $$
    Img^{(c)} = \left[\begin{matrix}
        pixel_{00} & pixel_{01}  & \cdots & pixel_{0m} \\
        pixel_{10} & pixel_{11}  & \cdots & pixel_{1m} \\
        \vdots & \vdots & \ddots & \vdots \\
        pixel_{n0} & pixel_{n1}  & \cdots & pixel_{nm} \\
    \end{matrix}\right]_{c}
    $$
    </p>
    
    com c = {red, green, blue}.

4) **Imagem com quantidade de cores reduzida:**

    Apartir dos passos anteriores, é definido uma nova imagem, a qual o total de cores deve estar definido no intervalo de 1 / 3  a 50% da quantidade de cores da imagem original.

## [Implementação] Apoximação por bins

1) **Leitura das imagens:**

```py
# Caminho para a imagem
images_path = {
    "araras": "/aatv03_lista-final/Q3/araras.png",
    "F1": "/aatv03_lista-final/Q3/F1.png",
    "green-water": "/aatv03_lista-final/Q3/green-water.png",
    "surf": "/aatv03_lista-final/Q3/surf.png",
}

imgs = {}
for key, path in images_path.items():
    img = cv2.imread(path)
    imgs[key] = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

2) **Funções:**

```py
def count_colores(
        image: np.ndarray
    ) -> int:
    """
    Conta o número de cores únicas em uma imagem RGB.

    Args:
        image (np.ndarray): Imagem RGB.

    Returns:
        int: Número de cores únicas.
    """
    # Converte a imagem para um array 2D
    pixels = image.reshape(-1, 3)
    # Conta as cores únicas
    unique_colors = np.unique(pixels, axis=0)
    return unique_colors.shape[0]

def reduce_colors(
        image: np.ndarray,
        bins: int = 4
    ) -> np.ndarray:
    """
    Reduz a quantidade de cores de uma imagem RGB, agrupando tons semelhantes.

    Args:
        image (np.ndarray): Imagem RGB.
        bins (int): Número de intervalos para quantização em cada canal (R, G, B).

    Returns:
        np.ndarray: Imagem com cores reduzidas.
    """
    # Calcula os limites dos intervalos
    bin_edges = np.linspace(
        0,
        256,
        bins + 1,
        dtype=np.int32
    )
    bin_centers = (
        (bin_edges[:(-1)] + bin_edges[(1):]) / 2
    ).astype(int)
    
    # Mapeia cada pixel para o centro do intervalo correspondente
    quantized_image = np.zeros_like(image)
    for i in range(3):  # Para cada canal (R, G, B)
        channel = image[:, :, i]
        indices = np.digitize(channel, bin_edges) - 1
        quantized_image[:, :, i] = bin_centers[indices]

    return quantized_image, bin_centers, bin_edges

def adjust_bins(
        image: np.ndarray,
        list_range: list=[50, 150],
        target_range: tuple = (1/3, 0.5)
    ) -> int:
    """
    Ajusta o número de bins para garantir que a quantidade de cores reduzidas
    esteja dentro do intervalo desejado.

    Args:
        image (np.ndarray): Imagem RGB.
        list_range (list): Intervalo de bins a serem testados (mínimo, máximo).
        target_range (tuple):
            Intervalo desejado (mínimo, máximo) como fração da quantidade de cores originais.

    Returns:
        int: Número de bins ajustado.
    """
    original_colors = count_colores(image)
    min_colors = int(original_colors * target_range[0])  # min % do numero de cores
    max_colors = int(original_colors * target_range[1])  # max % do numero de cores

    # Testar diferentes números de bins até atingir o intervalo desejado
    for bins in range(*list_range):
        reduced_image, _, _ = reduce_colors(image, bins)
        reduced_colors = count_colores(reduced_image)
        if min_colors <= reduced_colors <= max_colors:
            return bins

    # Caso não encontre, retorna o máximo de bins permitido
    return np.min(list_range)
```

3) **Redução de imagem:**

```py
# Aplicar a redução de cores nas imagens
reduced_imgs = {}
bins_per_image = {}
for key, img in imgs.items():
    # Ajustar dinamicamente os bins para cada imagem
    bin = adjust_bins(
        img,
        list_range=[50, 150, 10],  # parametro de procura de bins
        target_range=(1 / 3, 0.5)  # parametro de stop
    )#(1/3, 0.5))
    bins_per_image[key] = bin
    reduced_imgs[key] = reduce_colors(img, bins=bin)
```

4) **Salvando imagem de resultado:**

```py
for key, img in reduced_imgs.items():
    img = img[0]
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(path_assets / f"atv03_q03-reduced-{key}.png"), img_bgr)
```

5) **Visualização do resultado:**

```py
# Exibir as imagens originais e com cores reduzidas
fig, ax = plt.subplots(len(reduced_imgs), 2, figsize=(16, 10))

for idx, (key, img) in enumerate(reduced_imgs.items()):
    count_original = count_colores(imgs[key])
    count_reduced = count_colores(img[0])
    count_perc = 100 * (count_reduced / count_original)

    # Imagem original
    ax[idx, 0].imshow(imgs[key])
    ax[idx, 0].set_title(f"{key} - Original ({count_original} cores)")
    ax[idx, 0].axis("off")

    # Imagem com cores reduzida
    ax[idx, 1].imshow(img[0])
    ax[idx, 1].set_title(f"{key} - Reduzida ({count_reduced} cores | {count_perc:.2f}%)")
    ax[idx, 1].axis("off")

fig.tight_layout()
plt.show()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03_reduced_colors.png" alt="q04-i2-img" width="600"/>
</p>

6) **[Testes] Usando outros parametros:**

Testando outros parametros, com bins de menor tamanho, podemos ter resultados mais claros do efeito do algoritmo proposto. Vamos aplicar um teste para:

* `a`: 5 (bin inicial de tamanho 5);

* `b`: 50 (bin final de tamanho 50);

* `step`: 1 (salto entre as iterações de 1 aumento);

* `critério de parada`: entre 10% a 90% do total de cores da imagem original.

Dessa forma, temos os resultados abaixo:

```py
# Aplicar a redução de cores nas imagens
reduced_imgs = {}
bins_per_image = {}
for key, img in imgs.items():
    # Ajustar dinamicamente os bins para cada imagem
    bin = adjust_bins(
        img,
        list_range=[5, 50, 1],#[50, 150, 10],  # parametro de procura de bins
        target_range=(0.1, 0.9)# (1 / 3, 0.5)  # parametro de stop
    )#(1/3, 0.5))
    bins_per_image[key] = bin
    reduced_imgs[key] = reduce_colors(img, bins=bin)

# salvando imagem
for key, img in reduced_imgs.items():
    img = img[0]
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(path_assets / f"atv03_q03-reduced-{key}.png"), img_bgr)

# Exibir as imagens originais e com cores reduzidas
fig, ax = plt.subplots(len(reduced_imgs), 2, figsize=(16, 10))
for idx, (key, img) in enumerate(reduced_imgs.items()):
    count_original = count_colores(imgs[key])
    count_reduced = count_colores(img[0])
    count_perc = 100 * (count_reduced / count_original)

    # Imagem original
    ax[idx, 0].imshow(imgs[key])
    ax[idx, 0].set_title(f"{key} - Original ({count_original} cores)")
    ax[idx, 0].axis("off")

    # Imagem com cores reduzida
    ax[idx, 1].imshow(img[0])
    ax[idx, 1].set_title(f"{key} - Reduzida ({count_reduced} cores | {count_perc:.2f}%)")
    ax[idx, 1].axis("off")

fig.tight_layout()
plt.show()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03_reduced_colors_test2.png" alt="q04-i2-img" width="600"/>
</p>

Podemos notar que a qualidade da imagem ainda continua alta, com os contrastes ainda bem nitidos, mesmo com uma redução para 10% de cores da imagem original. Na figura abaixo é possivel notar o efeito que uma má seleção de parametros, como um range de bins com tamanhos pequenos podem afetar a resolução da imagem, além de um critério de parada mal selecionado. Podemos ver a diferença clara entre regiões da imagem de referencia "green-water" e "green-water" com quantidade de cores reduzida.

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03_img-comparison-test2.png" alt="q04-i2-img" width="600"/>
</p>


7) **Conclusão**

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
    <div style="text-align: center;">
        <a href="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-araras.png" target="_blank">
            <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-araras.png" alt="q04-i1-img" width="150"/>
        </a>
        <p><strong>Araras - Reduzida</strong></p>
    </div>
    <div style="text-align: center;">
        <a href="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-F1.png" target="_blank">
            <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-F1.png" alt="q04-i2-img" width="150"/>
        </a>
        <p><strong>F1 - Reduzida</strong></p>
    </div>
    <div style="text-align: center;">
        <a href="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-green-water.png" target="_blank">
            <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-green-water.png" alt="q04-i3-img" width="150"/>
        </a>
        <p><strong>Greem water - Reduzida</strong></p>
    </div>
    <div style="text-align: center;">
        <a href="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-surf.png" target="_blank">
            <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q03-reduced-surf.png" alt="q04-i3-img" width="150"/>
        </a>
        <p><strong>Surf - Reduzida</strong></p>
    </div>
</div>

**Obs.:** essa solução final mostrada trata-se do uso dos parâmetros:

* `a`: 50;

* `b`: 150;

* `step`: 10;

* `critério de parada`: entre 1 / 3 a 50% do total de cores da imagem original.

A solução proposta é robusta e flexivel, permite ao usuario a seleção de um percentual de cores ideal para que a imagem com uma quantidade de cores reduzida possua a partir da imagem original. Além disso, a redução foi significante, e ainda sim as imagens permanecem com seus contrastes,  mantendo a qualidade original da imagem.


# Questão 04

<strong>
Considere para esta questão as imagens: 

Textura1.png 

Textura2.png 

Textura3.png
</strong>

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_lista-final/Q4/Textura1.png" alt="q04-i1-img" width="150"/>
        <p><strong>Textura 1</strong></p>
    </div>
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_lista-final/Q4/Textura2.png" alt="q04-i2-img" width="150"/>
        <p><strong>Textura 2</strong></p>
    </div>
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_lista-final/Q4/Textura3.png" alt="q04-i3-img" width="150"/>
        <p><strong>Textura 3</strong></p>
    </div>
</div>

<strong>
As imagens Textura1 e Textura2 são de um mesmo material (suponha Classe 1), tendo sido tiradas de partes diferentes desse material. Já a imagem Textura 3 é de um material diferente (suponha Classe 2). Implemente um algoritmo, automático e com apenas uso de técnicas vistas na disciplina, que consiga classificar essas imagens entre as Classes 1 e 2. Não pode usar técnicas de classificação de aprendizagem de máquina. Manipulações matemáticas ou estatísticas usuais podem ser usadas, sendo devidamente justificadas.
</strong>

**R.:**

## Parte 01) Coeficiente de variação

Vamos analisar, em conjunto, a variabilidade em torno da média da transformada de fourier, utilizando do **Coeficiente de Variação**, cuja formula pode ser expressa abaixo

<p>
$$
CV_{\%} = \frac{\sigma}{\mu} \cdot 100
$$
</p>

aonde 

<p>
$$
\begin{cases}
\sigma: \text{ Desvio padrão da magnitude da transformada de fourier} \\
\mu: \text{ Média da magnitude da transformada de fourier}
\end{cases}
$$
</p>

Para tanto, considerando que o problema é binário, vamos fixar a imagem 1 (*Textura1*) como sendo uma referencia para a classe 1, e um threshold de permissão de 5% de variabilidade sobre essa imagem de referência, para que aquela textura pertença a classe 1. Vamos por partes, abaixo calculamos o desvio padrão para cada Textura.

```py
stats_values = {}
for key, value in imgs.items():
    stats_values[key] = {
        "media": float(value["img_fft"].mean()),
        "desvio": float(value["img_fft"].std())
    }
    stats_values[key]["cv"] = 100 * (stats_values[key]["desvio"] / stats_values[key]["media"])

data_stats = pd.DataFrame(stats_values).round(2)
data_stats
```

|          | Textura1 | Textura2 | Textura3 |
|----------|----------|----------|----------|
| **media** | 6.14     | 6.60     | 8.79     |
| **desvio** | 1.19     | 1.17     | 0.81     |
| **cv**     | 19.43    | 17.75    | 9.26     |

Dado os coeficientes de variação acima, como definido antes, vamos utilizar o coeficiente de variação da imagem *Textura1* como referência, ou seja, 19.43%. Dessa forma, com 5% de permissão de variabilidade sobre o coeficiente de variação, temos o limite superior de 19.43% + 5% = 24.43% e limite inferior de 19.43% - 5% = 14.43%, ou seja, para que a textura seja da classe 1, então  uma das condições para o algoritmo será o coeficiente de variação da imagem estar definido segundo a regra abaixo a regra abaixo:

<p>
$$
\begin{cases}
i\in \text{Classe 1}: \text{ se } 14.43 \leq cv_{i} \leq 24.43 \\
% i\in \text{Classe 2}: \text{ se } cv_{i} < 14.43 \text{ ou } cv_{i} > 24.43
\end{cases}
$$
</p>

Este método considera a variabilidade entre os valores de frequências na matriz de magnitudes de fourier, considerando o percentual de variabilidade em torno da média. Dessa forma, o algoritmo leva em consideração a média dos pixels e o desvio padrão da imagem.


## Parte 02) Estatística de Komolgorov-Smirnov 

Nesta parte do algoritmo, podemos utilizar a estatística calculada para o teste de Komolgorov-Smirnov, aonde o intuito é calcular a distância entre duas distribuições e mensurar quão proximas elas são. A formula é definida abaixo:

$$
D = max_{n}\{|F_{n}(x) - F(x)|\}
$$

Sendo "D" então como a máxima distãncia entre as distribuições acumuladas empirica amostrada (F<sub>n</sub>(x)) e a distribuição acumulada empirica a ser comparada (F(x)). No contexto atual, vamos considerar como F<sub>n</sub>(x) sendo a distribuição acumulada empirica magnitude obtida apartir da transformada de fourier para as imagens *Textura2* e *Textura3* a compararem com a distribuica acumulada empirica da magnitude da transformada de fourier para a imagem *Textura1* (F(x)). Para usar essa métrica, também é necessário selecionar um threshold, e dessa forma vamos fixar um valor de até 0.5 para ser parte da regra de decisão se a imagem será considerada da classe 1, logo:

<p>
$$
\begin{cases}
i \in \text{Classe 1}: \text{ se } D \leq 0.5
\end{cases}
$$
</p>
<!-- % i \in \text{Classe 2}: \text{ se } D > 0.5 -->

Abaixo, primeira imagem é feito a comparação da distribuição entre os histogramas das imagens, evidenciando claramente um distribuição afastada para a imagem *Textura3* longe das outras duas. Olhando para a segunda imagem, é possivel ver as distribuições de F<sub>n</sub>(x) para todas as texturas, mostrando a diferença de distribuições entre as classes.

```py
def ecdf(data):
    """Calcula a distribuição acumulada empírica (ECDF)."""
    sorted_data = np.sort(data)
    cumulative = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    return sorted_data, cumulative

img_refer = "Textura1"
ecdfs = {}
distances = {}
# Plots
fig, ax = plt.subplots(1, 2, figsize=(20, 8))
for key, img in imgs.items():
    dist = img["img_fft"].flatten()
    x, y = ecdf(dist)
    ecdfs[key] = {"x": x, "y": y}
    # Plotar a Distribuição de Densidade de Kernel (KDE)
    sns.kdeplot(dist, label=f"{key} - KDE", fill=True, alpha=0.3, ax=ax[0])
    
    # Calculo da estatística KS
    if key != img_refer:
        distances[key] = {
            "ks": float(ks_2samp(imgs[img_refer]["img_fft"].flatten(), dist).statistic)
        }

    # Plotar a Função de Densidade Acumulada (CDF)
    if key != img_refer:
        ax[1].plot(
            x,
            y,
            label="{} - ECDF - Distance: {:.2f}".format(key, distances[key]['ks']),
            linestyle="--"
        )
    else:
        ax[1].plot(
            x,
            y,
            label=f"{key} - ECDF",
            linestyle="--"
        )


# Configurar o gráfico
ax[0].set_title("Distribuição e Densidade Acumulada das Magnitudes da FFT")
ax[0].set_xlabel("Valores de Magnitude")
ax[0].set_ylabel("Densidade / Probabilidade Acumulada")
ax[1].set_title("Função de Densidade Acumulada (CDF)")
ax[1].set_xlabel("Valores de Magnitude")
ax[1].set_ylabel("Probabilidade Acumulada")
ax[1].set_ylim(0, 1)
for _ax in ax.flatten():
    _ax.spines[["top", "right"]].set_visible(False)
    _ax.legend()

fig.tight_layout()
plt.show()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q04-02.png" alt="q04-i2-img" width="600"/>
</p>

Como visto no gráfico, temos um valor de D = 0.21 para a *Textura2* e um valor de D = 0.82 para a *Textura3*, então pela regra de decisão definida, temos que a textura 2 satisfaz a condição da parte (2) para pertencimento a classe 1.

Agora, para o algoritmo, para pertencimento a classe 1 ou classe 2, precisa ser feito uma combinação das partes (1) e (2)

## Algoritmo) Conclusão

Por fim, o algoritmo aborda as partes (1) e (2) em conjunto, aonde cada método carrega uma checagem latente, sendo:


1) **Parte 01:** Essa parte carrega de forma intrisica uma checagem sobre a variabilidade em torno da média das frequências dos contrastes na imagem.

2) **Parte 02:** Analise de diferença entre distribuições acumuladas empiricas, utiliznado-se de metodos estatisticos mais robusto como a estatistica de komolgorov-smirnov, avaliando a distância global entre as distribuições.

Por fim, se:

<p>
$$
\begin{cases}
14.43 \leq cv_{i} \leq 24.43 \\
\text{ e } \\
% MAPE_{\%} \leq 25\% \\
% \text{ e } \\
D \leq 0.5
\end{cases}
$$
</p>

Então a imagem "i" será atribuido a classe 1.

Já para a classe 2, a imagem "i" será atribuido a ela se:

<p>
$$
\begin{cases}
cv_{i} < 14.43 \text{ ou } cv_{i} > 24.43 \\
\text{ ou } \\
% MAPE_{\%} > 25\% \\
% \text{ e } \\
D > 0.5
\end{cases}
$$
</p>

Perceba a existência de um "ou" na classificação da classe 2, ou seja, se apenas uma das condições do algoritmo não for valida, o algoritmo rejeita o pertencimento a classe 1, alocando a classe 2. Essa caracteristica ajuda a garantir um padrão homogeneo da classe 1, garantindo uma variabilidade controlada ainda (devido a parte 1 do algoritmo).

Logo, temos as condições acima para atribuir a imagem "i" para a classe 1 ou para a classe 2.


# Questão 05

<strong><u>Aplicação real:</u></strong>

<strong>A imagem Merge_Timex_BoaViagem.png foi tirada por uma câmera colocada no topo de um prédio na Av. Boa Viagem em Recife. Ela tira diversas fotos que são agrupadas, posteriormente. O objetivo é medir o avanço do mar na faixa de areia. A mancha preta na parte central superior da imagem é a câmera. As “manchas” inclinadas que vemos na faixa de areia são objetos (ou sombras) distorcidos pela lente da câmera. Veja a figura a seguir:</strong>



<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-00-00.png" alt="q05-00-00-img" width="600"/>
</p>

<strong>
Implemente um algoritmo automático e apenas com técnicas vistas na disciplina que detecte a região onde o mar encontra a faixa de areia. Por exemplo, seu resultado final poderia ser esse: 
</strong>

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-00-01.png" alt="atv03_q05-00-01-img" width="600"/>
</p>

<strong>
Ou esse (com a região marcada na imagem):
</strong>

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-00-02.png" alt="atv03_atv03_q05-00-02-img" width="600"/>
</p>

**R.:**


## **[Algoritmo] Explicação**

Durante o processo para detectarmos o avanço do mar na faixa de areia, vamos aplicar algumas ténicas de processamento de imagem, sendo elas as listadas abaixo:

1) **Conversão para HSV**
2) **Recorte da imagem**
3) **Filtro passa-baixa gaussiano**
4) **Dilatação**
5) **Binarização (OTSU)**
6) **Operação morofologica (Fechamento)**
7) **Operação morofologica (Abertura)**
8) **Canny**
9) **Resultado**


Os passos acima serão detalhados abaixo:

1) **Conversão para HSV**
Inicialmente, convertemos a imagem original RGB para o formato HSV.
Iremos selecionar o canal de saturação (S) para trabalhar, uma vez que essa saturação ajuda a evidenciar a transição entre a região de baixa saturação que é a areia para o de alta saturação que é o mar. Isso será particularmente util para o uso das técnicas seguintes.

2) **Recorte da imagem**
Aplicar um recorte da imagem mais proximo da região da praia, mais proximo da faixa de areia;

Esse recorte tem como objetivo diminuir a variação de contrastes, e aproximar o local de busca, que trata-se da faixa que o mar evidencia ao tocar a região da areia. Dessa forma, vamos aplicar uma sequência de técnicas para tentar delinear a fronteira entre mar e agua.


Será feito os processamentos a seguir em escala de cinza, baseado no canal de saturação obetido apartir do HSV.


3) **Filtro Passa-Baixa gaussiana:** a aplicação desse filtro tem como intuito causar um borramento na imagem, suavizando variações abruptas de intensidade e reduzindo ruídos de alta frequência. Esse processo facilita a separação das regiões de interesse, tornando as transições entre mar e areia mais suaves e destacando as estruturas principais. O uso desse filtro também afeta o resultado final, em caso de não usar, ele causa em passos futuros, em especifico no passo de binarização, alguns desniveis grandes na fronteira entre o mar e a areia.

    * **Parâmetros:**
        
        * &sigma; = 1
        * **kernel**: matriz 3x3 de uns.

4) **Dilatação:** aplicação de uma dilatação sobre o canal, considerando o kernel abaixo:

<p>
$$
Kernel_{(1)} = \left[\begin{matrix}
    1 & 1 & 1 \\
    1 & 1 & 1 \\
    1 & 1 & 1 \\
\end{matrix}\right]
$$
</p>

Essa aplicação tem como intuito dilatar as cores brancas para os vizinhos, com o intuito de expandir um pouco a fronteira entre areia e mar.


5) **Binarização (OTSU):** o método de OTSU foi utilizado para binarizar a imagem, com o intuito de conseguir deixar a região da areia mais branca e a região da praia mais escura, uma vez que ela soma dos passos anteriores, a imagem encontra-se um contraste maior entre as duas regiões. Isso será mostrado mais a frente.


6) **Operação morfologica (Fechamento):** será realizado um processo de fechamento com o intuito de preenchimento de falhas em contornos, em especial na fronteira entre mar e areia, preto e branco respectivamente, além de diminuir as areas de preto em especial as restantes na área da areia. Será considerado um kernel sendo uma matriz 7x7 composta por 1, ou seja:

<p>
$$
Kernel_{(2)} = \{1 \}_{7x7}
$$
</p>

Esse procedimento será aplicado um efeito em cascata, sendo aplicado por 5 iterações, ou seja, será aplicado 5 vezes.

7) **Operação morfologica (Abertura):** dado o passo anterior, será realizado uma abertura para suavizar o contorno da fronteira entre o branco e preto da áreia e agua, respectivamente, ajudando a remover ramificações restantes ao longo do mar, e expandindo alguma área de preto restante na região do mar. O mesmo kernel utilizado no passo anterior, será utilizado aqui também.

Esse procedimento será aplicado um efeito em cascata, sendo aplicado por 5 iterações, ou seja, será aplicado 5 vezes.

8) **Canny:** dado dos os passos todos anteriores, é obtido uma imagem com preto e branco, aonde é possivel notar a fronteira entre branco e preto, representando a fronteira entre mar e areia. Dado isso, é possivel aplicar um algoritmo para detecção de bordas, sendo ele o canny como o escolhido, para a separação dessa fronteira.

9) **Resultado:**  por fim, teremos a fronteira bem definida entre agua e areia, com as imagens sobrepostas como no primeiro exemplo de resposta da questão.

## **[Implementação] Código**


Antes de dar seguimento, vamos ler a iamgem:


```py
imgs = {
    "Merge_Timex_BoaViagem": cv2.imread(
        str(path_imgs_atv / "Q5" / "Merge_Timex_BoaViagem.png")
    )
}
img = cv2.cvtColor(imgs["Merge_Timex_BoaViagem"], cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(imgs["Merge_Timex_BoaViagem"], cv2.COLOR_BGR2HSV)
```

além disso, vamos definir os parâmetros a serem utilizados abaixo:

```py
# parametros
kernel_morph = np.ones((7, 7), np.uint8)  # kernel utilizado para operações morfologicas
kernel_dilate = np.ones((3, 3), np.uint8)  # kernel utilizado para dilatação 
kernel_gaussian = (3, 3)  # kernel utilizado para passa baixa gaussiana
sigma = 1  # sigma utilizado para operações morfologicas
iter_dilate = 1  # iterações de dilatação
iterations = 5  # iterações de operações morfologicas
lim_inf = 50  # corte inicial em x
lim_sup = 210  # corte final em x
c_selected = "S"  # canal a ser utilizado do HSV - Saturação (S)
threshold1 = 100  # valor minimo para o canny
threshold2 = 200  # valor maximo para o canny
```

1) **Conversão para HSV**

Abaixo temos a imagem a esquerda em RGB, e a direita defindia no espaço HSV.

```py
# Conversão para hsv
fig, ax = plt.subplots(2, 1, figsize=(16, 8))
ax[0].imshow(img)
ax[0].set_title("Imagem Original")
# ax[0].axis("off")
ax[1].imshow(img_hsv, cmap="gray")
ax[1].set_title("Imagem HSV")
# ax[1].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-01.png" alt="q05-01-img" width="600"/>
</p>


2) **Recorte da imagem**

Vamos fazer um recorte da imagem que iremos trabalhar para os proximos passos.

```py
# Recorte da imagem parte 1: 
img_cut_org = img[lim_inf:lim_sup, :]
img_cut_hsv = img_hsv[lim_inf:lim_sup, :]
fig, ax = plt.subplots(2, 1, figsize=(16, 4))
ax[0].imshow(img_cut_org)
ax[0].set_title("Imagem Original")
# ax[0].axis("off")
ax[1].imshow(img_cut_hsv, cmap="hsv")   
ax[1].set_title("Imagem HSV")
# ax[1].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-02.png" alt="q05-02-img" width="600"/>
</p>


Como mencionado anteriormente, vamos trabalhar com o canal de Saturação (S), e vamos trabalhar em tons de cinza. Dessa forma temos:


```PY
# Recorte da imagem parte2:
img_cut_hsv = {
    c: {
        "org": img[:, :, :],
        "hsv_cut": img_hsv[:, :, idx],
        "cut": img_hsv[lim_inf:lim_sup, :, idx]
    } for idx, c in  enumerate(["H", "S", "V"])
}

# Plotar resultado
fig, ax = plt.subplots(2, 1, figsize=(16, 8))
ax[0].imshow(img_cut_hsv[c_selected]["hsv_cut"], cmap="gray")
ax[0].set_title(f"Imagem HSV - Canal {c_selected}")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["cut"], cmap="gray")
ax[1].set_title(f"Recorte")
ax[1].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-03.png" alt="q05-03-img" width="600"/>
</p>

3) **Filtro Passa-Baixa gaussiana:**

Abaixo será aplicado o filtro passa-baixa gaussiano, considerando um &sigma; = 1, logo:

```PY
# Aplicando o filtro passa-baixa gaussiano
img_cut_hsv[c_selected]["processed"] = cv2.GaussianBlur(
    img_cut_hsv[c_selected]["cut"],
    kernel_gaussian,
    sigmaX=sigma
)

# Plotando o resultado
fig, ax = plt.subplots(2, 1, figsize=(16, 4))
ax[0].imshow(img_cut_hsv[c_selected]["cut"], cmap="gray")
ax[0].set_title(f"Recorte")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["processed"], cmap="gray")
ax[1].set_title(f"... + Passa-Baixa Gaussiano")
ax[1].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-04.png" alt="q05-04-img" width="600"/>
</p>

4) **Dilatação:**

Abaixo, aplicamos a dilatação considerando o kernel anteriormente citado.

```py
# Dilatação 
img_cut_hsv[c_selected]["processed_dilate"] = cv2.dilate(
    img_cut_hsv[c_selected]["processed"],
    kernel_dilate,
    iterations=iter_dilate
)

# Plotando o resultado
fig, ax = plt.subplots(2, 1, figsize=(16, 4))
ax[0].imshow(img_cut_hsv[c_selected]["processed"], cmap="gray")
ax[0].set_title(f"... + Passa-Baixa Gaussiano")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["processed_dilate"], cmap="gray")
ax[1].set_title(f"... + Dilatação")
ax[1].axis("off")
fig.tight_layout()
```
<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-05.png" alt="q05-05-img" width="600"/>
</p>

5) **Binarização (OTSU):**

Com a imagem dilatada anteriormente, vamos aplicar um processo de binarização utilizando do método do OTSU para seleção automática do threshold.

```py
# Binarização (OTSU)
_, img_cut_hsv[c_selected]["processed_dilate_bin"] = cv2.threshold(
    img_cut_hsv[c_selected]["processed_dilate"],
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Plotando o resultado
fig, ax = plt.subplots(2, 1, figsize=(16, 4))
ax[0].imshow(img_cut_hsv[c_selected]["processed_dilate"], cmap="gray")
ax[0].set_title(f"... + Dilatação")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["processed_dilate_bin"], cmap="gray")
ax[1].set_title(f"... + Binarização")
ax[1].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-06.png" alt="q05-06-img" width="600"/>
</p>

Perceba que ainda existem regiões de preto na parte superior (região da areia) e um pequeno espaco branco na região preta (região do mar), isso será tratado com os dois processos de operações morfologicas abaixo, Fechamento e Abertura, respectivamente.

6) **Operação morfologica (Fechamento):**

Vamos aplicar o fechamento, para tentar desaparecer com os pontos pretos da região superior da imagem e expandir alguns pontos brancos na região preta abaixo.

```py
# Operação morfologica (Fechamento)
img_cut_hsv[c_selected]["processed_dilate_bin_close"] = cv2.morphologyEx(
    img_cut_hsv[c_selected]["processed_dilate_bin"],
    cv2.MORPH_CLOSE,
    kernel_morph,
    iterations=iterations
)

# Plotando o resultado
fig, ax = plt.subplots(2, 1, figsize=(16, 4))
ax[0].imshow(img_cut_hsv[c_selected]["processed_dilate_bin"], cmap="gray")
ax[0].set_title(f"... + Binarização")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["processed_dilate_bin_close"], cmap="gray")
ax[1].set_title(f"... + Fechamento")
ax[1].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-07.png" alt="q05-07-img" width="600"/>
</p>

7) **Operação morfologica (Abertura):**

Aplicando a abertura com o intuito de suavização de contornos, e remoção de ramificações na região da fronteira entre branco e preto, além de tentar expandir a parte inferior restante de branco na região preta.


```py
# Operação morfologica (Abertura)
img_cut_hsv[c_selected]["processed_dilate_bin_close_open"] = cv2.morphologyEx(
    img_cut_hsv[c_selected]["processed_dilate_bin_close"],
    cv2.MORPH_OPEN,
    kernel_morph,
    iterations=iterations
)

# Plotando o resultado
fig, ax = plt.subplots(2, 1, figsize=(16, 4))
ax[0].imshow(img_cut_hsv[c_selected]["processed_dilate_bin_close"], cmap="gray")
ax[0].set_title(f"... + Fechamento")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["processed_dilate_bin_close_open"], cmap="gray")
ax[1].set_title(f"... + Abertura")
ax[1].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-08.png" alt="q05-08-img" width="600"/>
</p>


8) **Canny:**

Abaixo vamos aplicar o Canny na imagem resultante do passo anterior, adicionando um processo de dilatação apenas para visualizar de forma mais "robusta" a fronteira definida apos o canny.

```py
# Canny
img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny"] = cv2.Canny(
    img_cut_hsv[c_selected]["processed_dilate_bin_close_open"],
    threshold1=threshold1,
    threshold2=threshold2
)

# Canny dilated
img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny_dilated"] = cv2.dilate(
    img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny"],
    kernel_dilate,
    iterations=1
)


# Plotando o resultado
fig, ax = plt.subplots(3, 1, figsize=(16, 4))
ax[0].imshow(img_cut_hsv[c_selected]["processed_dilate_bin_close_open"], cmap="gray")
ax[0].set_title(f"... + Abertura")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny"], cmap="gray")
ax[1].set_title(f"... + Canny (Fronteira encontrada)")
ax[1].axis("off")
ax[2].imshow(img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny_dilated"], cmap="gray")
ax[2].set_title(f"Aplicando dilatação para destaque da borda")
ax[2].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-09.png" alt="q05-09-img" width="600"/>
</p>

9) **Resultado:**

Abaixo, vamos sobrepor apenas a fronteira entre mar e areia encontrada sobre a imagem original, com três imagens, sendo a primeira a original, a segunda sendo a borda encontrada, e a terceira com uma dilatação dessa borda, para melhor visualização.


```py
# Sobreposição no recorte

## Fronteira sem dilatação
img_cut_hsv[c_selected]["img_final_nodilate"] = img_cut_hsv[c_selected]["org"].copy()
img_cut_hsv[c_selected]["img_final_nodilate"][lim_inf:lim_sup, :, :][
    img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny"] > 0
] = [255] * 3
img_cut_hsv[c_selected]["cut_img_final_nodilate"] = img_cut_hsv[c_selected]["cut"].copy()
img_cut_hsv[c_selected]["cut_img_final_nodilate"][
    img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny"] > 0
] = 255


## Fronteira com dilatação
img_cut_hsv[c_selected]["img_final_dilated"] = img_cut_hsv[c_selected]["org"].copy()
img_cut_hsv[c_selected]["img_final_dilated"][lim_inf:lim_sup, :, :][
    img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny_dilated"] > 0
] = [255] * 3
img_cut_hsv[c_selected]["cut_img_final_dilated"] = img_cut_hsv[c_selected]["cut"].copy()
img_cut_hsv[c_selected]["cut_img_final_dilated"][
    img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny_dilated"] > 0
] = 255

# Plotando o resultado
fig, ax = plt.subplots(3, 1, figsize=(18, 10))
ax[0].imshow(img_cut_hsv[c_selected]["org"], cmap="gray")
ax[0].set_title("Imagem Original")
ax[0].axis("off")
ax[1].imshow(img_cut_hsv[c_selected]["img_final_nodilate"], cmap="gray")
ax[1].set_title(
    "Imagem com faixa do mar marcada"
)
ax[1].axis("off")
ax[2].imshow(img_cut_hsv[c_selected]["img_final_dilated"], cmap="gray")
ax[2].set_title(
    "Imagem com faixa do mar marcada (dilatação)"
)
ax[2].axis("off")

fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-10.png" alt="q05-10-img" width="600"/>
</p>

Acima, podemos ver que a fronteira foi encontrada, sendo bem definida, porém havendo alguns pontos de atenção a qual a fronteira encontra um pouco acima da linha do mar. Contudo, no geral, a fronteira foi bem definida para visualização do avanço do mar.

Abaixo podemos ver uma visão detalhada dos processamentos aplicados sobre o recorte no canal de saturação obtido pelo HSV:


```py
imgs_dict = {
    "Filtro Passa-Baixa Gaussiano": img_cut_hsv[c_selected]["processed"],
    "... + Dilatação": img_cut_hsv[c_selected]["processed_dilate"],
    "... + Binarização (OTSU)": img_cut_hsv[c_selected]["processed_dilate_bin"],
    "... + Fechamento": img_cut_hsv[c_selected]["processed_dilate_bin_close"],
    "... + Abertura": img_cut_hsv[c_selected]["processed_dilate_bin_close_open"],
    "... + Canny": img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny"],
    "... + Dilatação (Engrossar a fronteira)": img_cut_hsv[c_selected]["processed_dilate_bin_close_open_canny_dilated"],
    "S - Recorte com fronteira": img_cut_hsv[c_selected]["cut_img_final_dilated"],
}

## Plotando todas as imagens
fig, ax = plt.subplots(len(imgs_dict), 1, figsize=(16, 20))
for i, (key, img) in enumerate(imgs_dict.items()):
    ax[i].imshow(img, cmap="gray")
    ax[i].set_title(key)
    ax[i].axis("off")
fig.tight_layout()
```

<p align="center" >
    <img src="https://raw.githubusercontent.com/Manuelfjr/pdi/refs/heads/develop/assets/atv03_q05-11.png" alt="q05-11-img" width="600"/>
</p>