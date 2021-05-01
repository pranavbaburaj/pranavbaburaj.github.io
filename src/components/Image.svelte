<script lang="ts">
  interface Margins {
    top?: number;
    bottom?: number;
    rigth?: number;
    left?: number;
  }

  function createStyleString(data: Array<string>) {
    let css = '';
    for (let index = 0; index < data.length; index++) {
      css += data[index];
    }

    return css;
  }

  export let source: string;
  export let isProfile: boolean;
  export let text: string;
  export let viewportHeigth: number | null;
  export let margins: Margins;

  function createImageMargins(data: Margins): string {
    let array = [data.top, data.bottom, data.rigth, data.left];
    let keys = ['margin-top', 'margin-bottom', 'margin-right', 'margin-left'];
    let marginString = '';
    for (let index = 0; index < array.length; index++) {
      const currentMargin = array[index];
      if (currentMargin) {
        marginString += `${keys[index]}:${currentMargin}vh;`;
      }
    }

    return marginString;
  }

  let modalDisplay:string = "display:none;"

  function showImageModal() {
      modalDisplay = "display:block;"
  }

  let borderRadius: string = isProfile ? 'border-radius:50%;' : '';
  let height: string = viewportHeigth ? `height:${viewportHeigth}vh;` : '';
  let imageMargins: string = createImageMargins(margins);

  const css = createStyleString([borderRadius, height, imageMargins]);
</script>

<main>
  <img src={source} alt={text} title={text} style={css} on:click={showImageModal} />
  <div id="imageModal" class="modal" style={modalDisplay}>
    <span class="close" on:click={
        (event) => {
            modalDisplay = "display:none;";
        }
    }>&times;</span>
    <img class="modal-content" id="img" src={source} alt={text} />
  </div>
</main>

<style>
  img {
    cursor: pointer;
    transition: opacity 0.3s;
  }

  img:hover {
    opacity: 0.9;
  }

  /* The Modal (background) */
  .modal {
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 100px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: #36393F; /* Fallback color */
    background-color: #202225; /* Black w/ opacity */
    backdrop-filter: blur(5px);
  }

  /* Modal Content (Image) */
  .modal-content {
    margin: auto;
    display: block;
    width: 80%;
    max-width: 700px;
  }

  /* Caption of Modal Image (Image Text) - Same Width as the Image */
  #caption {
    margin: auto;
    display: block;
    width: 80%;
    max-width: 700px;
    text-align: center;
    color: #ccc;
    padding: 10px 0;
    height: 150px;
  }

  /* Add Animation - Zoom in the Modal */
  .modal-content,
  #caption {
    animation-name: zoom;
    animation-duration: 0.6s;
  }

  @keyframes zoom {
    from {
      transform: scale(0);
    }
    to {
      transform: scale(1);
    }
  }

  /* The Close Button */
  .close {
    position: absolute;
    top: 15px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    transition: 0.3s;
  }

  .close:hover,
  .close:focus {
    color: #bbb;
    text-decoration: none;
    cursor: pointer;
  }

  /* 100% Image Width on Smaller Screens */
  @media only screen and (max-width: 700px) {
    .modal-content {
      width: 100%;
    }
  }

  .hideModal {
      z-index : -1;
      opacity : 0;
      animation : hide .25s;
      transform :scale(0);
  }

  @keyframes hide {
      from{
          z-index : 2;
          transform : scale(1);
          opacity : 1;
      } to {
          z-index : -1;
          transform : scale(1);
          opacity : 0;
      }
  }
</style>
