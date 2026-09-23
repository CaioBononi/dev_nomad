import firebase from '../firebase/firebase'
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } from 'firebase/auth'

const auth = getAuth(firebase)

    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            console.log(`User.UID: ${substring(user.uid, 0, 6)}**********************`)
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
        });

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            console.log(`User.UID: ${substring(user.uid, 0, 6)}**********************`)
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
        });
