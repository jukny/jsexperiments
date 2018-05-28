template = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>##name##</title>
    <link href="css/bootstrap/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
  </head>
  <body>

    <div class="container-fluid">
	<div class="row">
		<div class="col-md-12">
			<img alt="No image found for ##name##" id="images" src="#" class="rounded">
		</div>
	</div>
	<div class="row">
		<div class="col-md-12">
			<p class="captions">
			</p>
			<form id="nav" role="form" class="form-inline">
				<div class="form-group">					 
					<label for="IndexInput">
						Image Index 
					</label>
					<input type="email" class="form-control" id="IndexInput">
				</div>
				<button id="update" type="button" class="btn btn-primary">
					Go to
				</button>
			</form>
		</div>
	</div>
</div>

    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap/bootstrap.min.js"></script>
    <script src="images/##name##/captions.js"></script>
    <script src="images/##name##/images.js"></script>
    <script src="js/story.js"></script>
  </body>
</html>"""