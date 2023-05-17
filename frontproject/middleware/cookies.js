
export default ( { store, req } ) => {
    try {
        if(req) {
            const COOKIES = Object.fromEntries(req.headers.cookie.split('; ').map(x => decodeURIComponent(x).split('=')))
    
            if(COOKIES['leg__token']) {
                let data = {}
                data['token'] = COOKIES['leg__token'] ? COOKIES['leg__token'] : undefined
                data['user_id'] = COOKIES['leg__id'] ? COOKIES['leg__id'] : undefined
                data['email'] = COOKIES['leg__email'] ? COOKIES['leg__email'] : undefined
                data['user_type'] = COOKIES['leg__user_type'] ? COOKIES['leg__user_type'] : ''
    
                if( !Object.values(data).includes(undefined) ) {
                    store.commit('auth/user', data)
                }
            }
        }
    }
    catch {
        console.info('INCOGNITO MODE ENABLED')
    } 
}