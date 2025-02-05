# React + TypeScript

## Como rodar o projeto

1. Instale as dependências com:
   ```sh
   npm install
   ```
2. Rode o projeto com:
   ```sh
   npm run dev
   ```

## Estrutura de pastas

```
/my-react-app
│── /public
│── /src
│   ├── /assets       # Imagens, ícones, estilos globais, fontes etc.
│   ├── /pages        # Páginas principais da aplicação
│   ├── /routes       # Configuração das rotas da aplicação
│   ├── /shared       # Recursos compartilhados
│   │   ├── /components # Componentes reutilizáveis
│   │   ├── /contexts   # Contextos do React (React Context API)
│   │   ├── /hooks      # Hooks personalizados
│   │   ├── /services   # Serviços de API, requisições HTTP etc.
│   ├── App.tsx        # Componente principal da aplicação
│   ├── main.tsx       # Ponto de entrada do React
│   ├── vite.config.ts # Arquivo de configuração do Vite (caso use Vite)
│── package.json
│── tsconfig.json      # Configuração do TypeScript (caso use TypeScript)
│── .eslintrc.js       # Configuração do ESLint (se necessário)
│── .gitignore
```

## Meu primeiro componente

O componente principal é o `App.tsx`. Ele deve importar e organizar os demais componentes, mas não conter toda a lógica da aplicação, pois o React incentiva a componentização para manter o código modular, legível e organizado.

### Exemplo de componente

```tsx
import React from "react";

const Lista: React.FC = () => {
  const handleClick = () => {
    window.alert("Olá, mundo!");
  };

  return (
    <div>
      <button onClick={handleClick}>Clique aqui</button>
    </div>
  );
};

export default Lista;
```

## Importando e exportando componentes

Vamos importar o componente Lista para o App. Perceba que, ao final do código, temos o `export default 'nome do componente'`.
Com isso, podemos utilizá-lo em outras partes do projeto.

### Passos:
1. Importar o componente.
2. Colocar o componente dentro do JSX.

**Obs:** Perceba que o componente se parece com uma tag HTML e sempre começa com letra maiúscula.

```tsx
import "./App.css";
import Lista from "./shared/components/Lista/Lista";

function App() {
  return (
    <>
      <Lista />
    </>
  );
}

export default App;
```

## TypeScript no JSX

A sintaxe JSX permite que você escreva tags similares ao HTML dentro de um arquivo TypeScript, mantendo a lógica de renderização e o conteúdo no mesmo local. Às vezes, você pode querer adicionar um pouco de lógica TypeScript ou referenciar uma propriedade dinâmica dentro deste bloco de tags. Nessa situação, você pode usar chaves em seu JSX para abrir uma janela para o TypeScript.

### Exemplo 1

```tsx
import React from "react";
import imagem from "../../../assets/Captura_de_Tela.png";

export const Imagem: React.FC = () => {
  const description = "captura de tela";
  return (
    <div>
      <img src={imagem} alt={description} />
    </div>
  );
};
```

### Exemplo 2

```tsx
const Laranjas: React.FC = () => {
  const quantidadeDeLaranjas = 20;
  return (
    <div>
      <p>A quantidade de laranjas é {quantidadeDeLaranjas}</p>
    </div>
  );
};
```

## Passando Props a um Componente

Props são as informações que você passa usando uma tag JSX. Por exemplo, className, src, alt, width e height são algumas das props que você pode passar a uma `<img>`.

Componentes do React usam props para se comunicar um com o outro. Todo componente pai pode passar alguma informação aos seus filhos por meio das props. Props podem lembrar atributos HTML, mas você pode passar qualquer valor JavaScript por meio delas, incluindo objetos, arrays e funções.

### Criando componente com Props

```tsx
import React from "react";

interface PropsButton {
  onClick: () => void;
  children: React.ReactNode;
  disabled?: boolean;
}

export const PropsButton: React.FC<PropsButton> = ({
  onClick,
  children,
  disabled,
}) => {
  return (
    <div>
      <button disabled={disabled} onClick={onClick}>
        {children}
      </button>
    </div>
  );
};
```

**Obs:** No React com TypeScript, devemos criar uma interface com as propriedades que queremos. Assim, passamos essas propriedades para o componente. Com a tipagem, teremos autocomplete e indicação de erro caso falte alguma propriedade. Para tornar uma propriedade opcional, basta adicionar `?` ao final do nome da propriedade antes dos `:`.

### Passando as Props para o componente

```tsx
import { FaFacebook } from "react-icons/fa";
import "./App.css";
import { PropsButton } from "./shared/components";

function App() {
  const handleClick = () => {
    window.alert("Olá, mundo");
  };

  return (
    <>
      <PropsButton onClick={handleClick} disabled={false}>
        <FaFacebook /> Facebook
      </PropsButton>
    </>
  );
}

export default App;
```

**Obs:** O children permite que você insira qualquer tipo de conteúdo dentro do componente, seja texto, ícones, ou outros componentes React.

**Obs:** No componente App, passamos as propriedades para o `PropsButton`. Assim, ao clicar, aparece um alerta com "Olá, mundo". O botão terá um ícone do Facebook e estará habilitado. O uso das props nos permite customizar e reutilizar o componente em vários locais, adaptando-o conforme a necessidade.

### Renderização Condicional

Seus componentes frequentemente precisarão exibir coisas diferentes dependendo de diferentes condições. No React, você pode renderizar condicionalmente JSX usando sintaxe do Typescript, como declarações if, e operadores ? : e &&.

## Exemplo

```tsx
import React, { useState } from "react";

const Condicional: React.FC = () => {
  const [soma, setsoma] = useState(0);
  const [mostrar, setMostrar] = useState(false);

  const Somar = () => {
    setsoma((prev) => prev + 1);
  };

  const Visualizar = () => {
    setMostrar((prev) => !prev);
  };

  return (
    <div>
      <button onClick={Somar}>Somar</button>
      <p>{soma}</p>
      <button onClick={Visualizar}>Mostrar</button>

      {mostrar && <p>mostrando </p>}

      {mostrar ? <p>Se mostrar for True </p> : <p>Se mostrar for false</p>}
    </div>
  );
};

export default Condicional;
```

**Obs:** Perceba que estamos usando o usestate, com ele temos variaveis de estado.
No React, as variáveis de estado são geralmente usadas para armazenar informações que determinam a aparência ou o comportamento de um componente em determinado momento. Quando o valor de uma variável de estado muda, o React automaticamente atualiza a UI para refletir a nova informação.
A primeira informação é a variável onde ficará armazenado os dados, e a função setAlgo será utilizada para atualizar essa variável

Dentro do jsx Fizemos a renderização condicional de duas formas:

1.

```tsx
{
  mostrar && <p>mostrando </p>;
}
```

Assim ocorre o seguinte: se a variável de estado mostrar for True,
será exibido o paragrafo escrito mostrando

2.

```tsx
{
  mostrar ? <p>Se mostrar for True </p> : <p>Se mostrar for false</p>;
}
```

Assim ocorre o seguinte: se mostrar for true, aparece o paragrafo escrito se mostrar for true, senão,
aparece o paragrafo escrito se mostrar for false

## Renderização de listas

É comum a necessidade de se exibir vários componentes semelhantes a partir de uma coleção de dados. Você pode usar os métodos de array Typescript para manipular um array de dados.

### Exemplo

```tsx
import React from "react";

interface person {
  nome: string;
  idade: number;
}

const RenderList: React.FC = () => {
  const lista = [
    "item 11",
    "item 22",
    "item 33",
    "item 44",
    "item 55",
    "item 66",
  ];
  const personList: person[] = [
    {
      nome: "jonas",
      idade: 20,
    },
    {
      nome: "Ernesto",
      idade: 20,
    },
    {
      nome: "Tiago",
      idade: 22,
    },
    {
      nome: "Lucas",
      idade: 22,
    },
  ];

  const filteredPersonList = personList.filter((person) => person.idade === 20);

  return (
    <div>
      <ul>
        {lista.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
      <ul>
        {personList.map((person, index) => (
          <>
            <li key={index}>Nome:{person.nome}</li>
            <li>Idade:{person.idade}</li>
          </>
        ))}
      </ul>
      <ul>
        {filteredPersonList.map((person, index) => (
          <>
            <li key={index}>Nome:{person.nome}</li>
            <li>Idade:{person.idade}</li>
          </>
        ))}
      </ul>
    </div>
  );
};

export default RenderList;
```

Entendendo o código:

1.Definindo os arrays: Temos dois arrays: um de strings (lista) e outro de objetos (personList). A ideia é transformar esses arrays em listas HTML dinâmicas, onde cada item será representado por um elemento <li>.

2.lista: contém simples strings, como "item 11", "item 22", etc.
personList: é uma lista de objetos representando pessoas, cada uma com nome e idade.
Usando o map(): O método map() é utilizado para percorrer os dois arrays e gerar um novo array de elementos JSX (que são componentes React). O map() aplica uma função a cada item do array e retorna um novo array de elementos com base no que você definiu.

No primeiro exemplo, estamos usando o map() para gerar uma lista de <li> com os itens do array lista.
No segundo exemplo, estamos gerando uma lista de <li> para cada pessoa em personList, exibindo o nome e a idade de cada uma.
No terceiro exemplo, estamos filtrando a personList para obter apenas as pessoas com idade igual a 20 e, em seguida, renderizando a lista filtrada de maneira similar.

3.A chave (key) para cada item: No React, quando estamos renderizando uma lista de elementos, é importante fornecer uma chave única para cada item da lista, para que o React possa identificar qual item foi alterado, removido ou adicionado. Nesse caso, estamos utilizando o index do array como a chave, embora seja mais recomendado usar um identificador único (por exemplo, um id de cada item) quando possível, para garantir a eficiência na renderização.
