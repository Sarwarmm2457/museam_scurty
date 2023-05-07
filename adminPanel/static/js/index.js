const circles = document.querySelectorAll('.circle');
const texts = document.querySelectorAll('.text');
const localStorageKeyPrefix = 'device_state_';

circles.forEach((circle, index) => {
  const checkbox = circle.parentElement.querySelector('input[type="checkbox"]');
  const localStorageKey = `${localStorageKeyPrefix}${index}`;

  // Initialize checkbox and circle based on local storage state
  const storedState = localStorage.getItem(localStorageKey);
  if (storedState !== null) {
    checkbox.checked = (storedState === 'on');
    circle.classList.toggle('on', checkbox.checked);
    circle.classList.toggle('off', !checkbox.checked);
    if (checkbox.checked) {
    } else {
    }
  }

  // Toggle circle status and text based on checkbox
  checkbox.addEventListener('change', (event) => {
    const isOn = event.target.checked;
    circle.classList.toggle('on', isOn);
    circle.classList.toggle('off', !isOn);
    if (isOn) {
      document.getElementById('photo_value').innerText = photo_value
    } else {
      document.getElementById('photo_value').innerText = 'oweinfeiwun'
    }

    // Store device state in local storage
    localStorage.setItem(localStorageKey, isOn ? 'on' : 'off');
  });
});
