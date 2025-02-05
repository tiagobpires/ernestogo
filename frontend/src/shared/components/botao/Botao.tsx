import React, { useState } from "react";

const NumberInput: React.FC = () => {
  const [value, setValue] = useState<string>("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const inputValue = e.target.value;

    if (inputValue === "") {
      setValue(inputValue);
      return;
    }

    const newValue = Number(inputValue);

    if (newValue < 0) {
      setValue("0");
    } else if (newValue > 24) {
      setValue("24");
    } else {
      setValue(inputValue);
    }
  };

  return (
    <div>
      <input
        type="number"
        value={value}
        onChange={handleChange}
        min={0}
        max={24}
      />
      <p>Valor: {value}</p>
    </div>
  );
};

export default NumberInput;
