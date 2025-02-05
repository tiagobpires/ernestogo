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
    </div>
  );
};

export default Condicional;
