# React + Typescript

1. Instalar as depêndencias com npm install

2. Rodar utilizando o comando npm run dev

# Estrutura de pastas

/my-react-app
│── /public
│── /src
│ ├── /assets # Imagens, ícones, estilos globais, fontes etc.
│ ├── /pages # Páginas principais da aplicação
│ ├── /routes # Configuração das rotas da aplicação
│ ├── /shared # Recursos compartilhados
│ │ ├── /components # Componentes reutilizáveis
│ │ ├── /contexts # Contextos do React (React Context API)
│ │ ├── /hooks # Hooks personalizados
│ │ ├── /services # Serviços de API, requisições HTTP etc.
│ ├── App.tsx # Componente principal da aplicação
│ ├── main.tsx # Ponto de entrada do React
│ ├── vite.config.ts # Arquivo de configuração do Vite (caso use Vite)
│── package.json
│── tsconfig.json # Configuração do TypeScript (caso use TypeScript)
│── .eslintrc.js # Configuração do ESLint (se necessário)
│── .gitignore

# Meu primeiro componente

O componente principal é o App.tsx. Ele deve importar e organizar os demais componentes, mas não conter toda a lógica da aplicação, pois o React incentiva a componentização para manter o código modular, legível e organizado.

const Lista: React.FC = () => {
const lucasGay = () => {
window.alert("olá mundo");
};

const numero = 2;
return (

<div>
<button onClick={lucasGay}>Aperte {numero}</button>
<P>olá mundo </p>
</div>
);
};

export default Lista;
