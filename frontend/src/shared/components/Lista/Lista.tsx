const Lista: React.FC = () => {
  const lucasGay = () => {
    window.alert("lucas gay");
  };

  const numero = 2;
  return (
    <div>
      <button onClick={lucasGay}>Aperte {numero}</button>
    </div>
  );
};

export default Lista;
