from flask import Flask

import os

app = Flask(__name__)

@app.route('/')

def hello_world():

    return """

<!DOCTYPE html>

<html lang="en">

<body>

    <div class="container" style="bg-dark text-red text-center py-3 mt-5">

        <a href="#" class="card">

            <p>

	    <center>	        <br /><br />

<pre style="font-size:18px; line-height:20px;">

███████╗ ██████╗ ███╗   ██╗██╗   ██╗

██╔════╝██╔═══██╗████╗  ██║██║   ██║

███████╗██║   ██║██╔██╗ ██║██║   ██║

╚════██║██║   ██║██║╚██╗██║██║   ██║

███████║╚██████╔╝██║ ╚████║╚██████╔╝

╚══════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ 

</pre>

	        <br /><br />

		</center>

            </p>

        </a>

    </div>

	<br></br>

        <center>

	<footer class="bg-dark text-white text-center py-3 mt-5">

		<div class="footer__copyright">

            <p class="footer__copyright-info">

                © 2025 Video Downloader. All rights reserved.

            </p>

        </div>

    </footer>

    </center>

</body>

</html>

"""

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
    
