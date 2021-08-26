<template>
  <div>
    <h1>Heartbeat demo</h1>
    <br />
    <p>
      This demo runs a simple variant of rPPG directly in your browser to
      measure your heart rate based on subtle changes in skin color.
    </p>
    <p>
      For best results, try in a constantly well lit space with minimal device
      and subject motion.
    </p>
    <br />
    <div>
      <video hidden id="webcam" width="640" height="480"></video>
      <canvas id="canvas" width="640" height="480"></canvas>
    </div>
  </div>
</template>
<script>
import Heartbeat from "/public/static/heartbeat.js";
export default {
  data: () => ({}),
  mounted() {
    const BASE_URL = process.env.BASE_URL;
    const faceAPI = document.createElement("script");
    faceAPI.setAttribute("src", `${BASE_URL}/static/face-api.min.js`);
    document.head.appendChild(faceAPI);
    
    const demo = new Heartbeat(
      "webcam",
      "canvas",
      `${BASE_URL}/static/haarcascade_frontalface_alt.xml`,
      30,
      6,
      250
    );

    let ready = this.loadOpenCv(`${BASE_URL}/static/opencv.js`);
    ready.then(() => demo.init());
  },

  methods: {
    async loadOpenCv(uri) {
      return new Promise(function(resolve) {
        console.log("starting to load opencv");
        var tag = document.createElement("script");
        tag.src = uri;
        tag.async = true;
        tag.type = "text/javascript";
        tag.onload = () => {
          cv["onRuntimeInitialized"] = () => {
            console.log("opencv ready");
            resolve();
          };
        };
        tag.onerror = () => {
          throw new URIError("opencv didn't load correctly.");
        };
        var firstScriptTag = document.getElementsByTagName("script")[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
      });
    },
  },
};
</script>
