<script>
  let message;
  fetch("http://192.168.32.42:8000/hello").then((response) => {
    response.json().then((json) => {
      message = json.message;
    });
  }); 
</script>
<h1>{message}</h1>