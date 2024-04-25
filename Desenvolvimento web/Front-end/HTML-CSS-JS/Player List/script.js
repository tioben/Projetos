// Variáveis globais
const section = document.getElementById("section");
const delPlayerForm = document.querySelector('#del-player-form');
const addPlayerForm = document.querySelector('#add-player-form');

// POO da aplicação
class Player {
  constructor(nickname, level, vocation, world, imgSRC) {
    this.nickname = nickname;
    this.level = level;
    this.vocation = vocation;
    this.world = world;
    this.imgSRC = imgSRC;
  }
}

let playerList = [
  new Player("zope", 16, "knight", "Retro-OpenPVP", "img/zope.gif"),
  new Player("tioben", 102, "sorcerer", "OpenPVP", "img/tioben.gif"),
  new Player("matuezin", 81, "druid", "OpenPVP", "img/matuezin.gif"),
  new Player("bluzu", 408, "paladin", "OptionalPVP", "img/bluzu.gif"),
  new Player("maikin", 8, "paladin", "Retro-HardcorePVP", "img/maikin.gif"),
  new Player("diguin", 28, "druid", "Retro-HardcorePVP", "img/diguin.gif")
];

// Função para renderizar os players na main
function viewPlayers() {
  section.innerHTML = "";
  for (let item of playerList) {
    var playerContainer = document.createElement('div');
    playerContainer.innerHTML = `
    <div class="player-container">
        <div class="image-container">
        ${item.imgSRC ? `<img src="${item.imgSRC}" alt="char-img">` : ''}
        </div>
        <ul>
          <li>Nickname: ${item.nickname}</li>
          <li>Vocation: ${item.vocation}</li>
          <li>Level: ${item.level}</li>
          <li>World: ${item.world}</li>
        </ul>
    </div>
    `;
    section.appendChild(playerContainer); 
  }
  return section;
}

// Função para adicionar player na tela
function addPlayer(nickname, vocation, level, world, imgSRC){
  playerList.unshift(new Player(nickname, level, vocation, world, imgSRC));
  viewPlayers();
}

// Função de validação do nickname personalizada
function nicknameValidation (nickname){

  // Variáveis de validação
  let isNicknameRepeated = false;
  let onlySpace = false;
  let spaceInStartOrAnd = false;
  const regex = /^[\s]+|[\s]+$/g;

  // Este nickname já existe?
  for (let item of playerList) {
    if (nickname.trim() === item.nickname) {
      isNicknameRepeated = true;
      break;
    }
  }

  // Tem apenas espaços?
  if (nickname.trim() === "") {
    onlySpace = true;
  }

  // Tem espaço no começo ou no fim?
  if(regex.test(nickname)){
    spaceInStartOrAnd = true;
  };

  // Retornos
  if(isNicknameRepeated){
    return "Nickname existente!";
  }
  else if(onlySpace){
    return "Não é permitido:\n Apenas espaços\n Espaços no começo\n Espaços no fim";
  }
  else if (spaceInStartOrAnd){
    return "Não é permitido:\n Apenas espaços\n Espaços no começo\n Espaços no fim";
  }
  else if((isNicknameRepeated == false) && (onlySpace == false) && (spaceInStartOrAnd == false)){
    return nickname;
  }

}

// Lógica para enviar addformulario para funcao addPlayer 
addPlayerForm.addEventListener('submit', function (e) {
  e.preventDefault(); // Impede o envio padrão do formulário (recarregar a página)

  const nickname = document.querySelector('#add-nickname').value;
  const vocation = document.querySelector('#add-vocation').value;
  const level = parseInt(document.querySelector('#add-level').value);
  const world = document.querySelector('#add-world').value;

  // Obtenha o arquivo de imagem selecionado pelo usuário
  const imageInput = document.querySelector('#upload-image');
  const imageFile = imageInput.files[0];

  if (nicknameValidation(nickname) === nickname) {
    if (imageFile) {
      // Se um arquivo de imagem foi selecionado, faça a leitura
      const reader = new FileReader();
      reader.onload = function () {
        const imageDataURL = reader.result;

        const newPlayer = new Player(nickname, level, vocation, world, imageDataURL);
        playerList.unshift(newPlayer);
        viewPlayers();
        addPlayerForm.reset();
      };
      reader.readAsDataURL(imageFile);
    } else {
      // Se nenhum arquivo de imagem foi selecionado, crie um novo jogador sem imagem
      const newPlayer = new Player(nickname, level, vocation, world, null); // Passa null como imagem
      playerList.unshift(newPlayer);
      viewPlayers();
      addPlayerForm.reset();
    }
  } else {
    alert(nicknameValidation(nickname));
  }
});

// Função deletar player da tela
function delPlayer(nickname) {
  const indexToRemove = playerList.findIndex(item => item.nickname === nickname);
  if (indexToRemove !== -1) {
    playerList.splice(indexToRemove, 1); // Remove 1 elemento a partir do índice encontrado
  }else{
    alert("Nenhum player encontrado");
  }

  viewPlayers()
}

// Lógica para enviar delformulário para função delPlayer
delPlayerForm.addEventListener('submit', function (e) {
  
  e.preventDefault(); // Impede o envio padrão do formulário (recarregar a página)

  const nickname = document.querySelector('#del-nickname').value;

  delPlayer(nickname);

  delPlayerForm.reset();
});

// Atribuindo lógica aos botões para abrir tela ao clicar em "adicionar jogador" ou "remover jogador" e fechar quando clicar em "X"
function buttonsAddRem(){
  const addButton = document.getElementById('add-button');
  const delButton = document.getElementById('del-button');
  const closeButton = document.getElementById('close-button');
  const div1 = document.getElementById('add-player');
  const div2 = document.getElementById('del-player');

  addButton.addEventListener('click', function (e) { //"Adicionar jogador"
    e.preventDefault();
    div1.style.display = 'block';
    div2.style.display = 'none';
    closeButton.style.display = "block";
  });

  delButton.addEventListener('click', function (e) { //"Remover jogador"
    e.preventDefault();
    div1.style.display = 'none';
    div2.style.display = 'block';
    closeButton.style.display = "block";
  });

  closeButton.addEventListener('click', function (e) { //"X"
    e.preventDefault();
    div1.style.display = 'none';
    div2.style.display = 'none';
    closeButton.style.display = "none";
  });
}

// Ativando funções essenciais
buttonsAddRem(); // Lógica dos botões "Adicionar jogador" e "Remover jogador"
viewPlayers(); // Renderizando primeira lista da página



