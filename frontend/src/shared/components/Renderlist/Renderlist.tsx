import React from "react";

const RenderList: React.FC = () => {
  const lista = [
    "item 11",
    "item 22",
    "item 33",
    "item 44",
    "item 55",
    "item 66",
  ];

  return (
    <div>
      <ul>
        {lista.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default RenderList;
