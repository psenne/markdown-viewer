from app import db, ma



# class PostSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "title", "content")
#         model = Post


# post_schema = PostSchema()
# posts_schema = PostSchema(many=True)


class DocumentSchema(ma.Schema):
    class Meta:
        fields = ("uuid", "text")

document_schema = DocumentSchema()
documents_schema = DocumentSchema(many=True)


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, unique=True)
    text = db.Column(db.Text)
    createDate = db.Column(db.DateTime)
    modifiedDate = db.Column(db.DateTime)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Document %s>' % self.uuid

    # def serialize(self):
    #     return {'uuid': self.uuid, 'text': self.text}



class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "emailAddress")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emailAddress = db.Column(db.String(120), unique=True, nullable=False)
    providerToken = db.Column(db.String(255), unique=True, nullable=False)
    createDate = db.Column(db.DateTime)
    publicKey = db.relationship('AuthorizedKey', backref='user', lazy=True)
    document = db.relationship('Document', backref='user', lazy=True)

    def __repr__(self):
        return '<User %s>' % self.emailAddress

    # def serialize(self):
    #     return {'id': self.id, 'emailAddress': self.emailAddress}


class AuthorizedKeySchema(ma.Schema):
    class Meta:
        fields = ("userId", "publicKey")

authorizedKey_schema = AuthorizedKeySchema()
authorizedKeys_schema = AuthorizedKeySchema(many=True)

class AuthorizedKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publicKey = db.Column(db.Text)
    createDate = db.Column(db.DateTime)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<AuthorizedKey %s>' % self.id

    # def serialize(self):
    #     return {'userId': self.userId, 'publicKey': self.publicKey}
