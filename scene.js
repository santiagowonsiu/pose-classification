const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
const geometry = new THREE.BoxGeometry(1, 1, 1); // Dimensions of the cube
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // Green color
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();
