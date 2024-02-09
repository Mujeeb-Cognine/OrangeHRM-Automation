def build = currentBuild
def buildUrl = build.absoluteUrl

def subject = "Jenkins Build Failed: ${build.fullDisplayName}"
def body = """
    <html>
    <body>
        <p>Dear User,</p>
        <p>The Jenkins build <a href="${buildUrl}">${build.fullDisplayName}</a> has failed.</p>
        <p>Please check the build logs for more details.</p>
        <p>Best regards,<br>Jenkins CI</p>
    </body>
    </html>
"""

return [subject: subject, body: body]
