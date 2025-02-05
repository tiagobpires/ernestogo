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

