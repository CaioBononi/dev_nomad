export class User {
    constructure(uid, displayName, email, emailVerified, phoneNumber, photoURL, disable, password, cratedAt, updatedAt){
        this.uid = uid
        this.displayName = displayName || ''
        this.email = email
        this.emailVerified = emailVerified || false
        this.phoneNumber = phoneNumber || ''
        this.photoURL = photoURL || ''
        this.disable = disable || false
        this.password = password
        this.cratedAt = cratedAt || new Date()
        this.updatedAt = updatedAt || new Date()
    }
}