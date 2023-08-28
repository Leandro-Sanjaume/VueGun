export enum AuthErrorType {
    NoError = 'NoError',
    IncompleteFields = 'INCOMPLETE_FIELDS',
    FirebaseAuthError = "FIREBASE_ERROR",
    UnknownError = "UNKNOWN_ERROR"
};

export type AuthError = {
    type: AuthErrorType;
    msg: string;
};
