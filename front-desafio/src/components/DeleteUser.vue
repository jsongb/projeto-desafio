<template>
    <!-- Componente de modal para confirmação de exclusão do usuário -->
    <div>
        <b-modal id="delete-user" title="Remover usuário" hide-header size="sm" @ok="removeUser" centered cancel-title="Cancelar">
            <b-row>
                <b-col>
                    <h4>
                        Deseja remover o usuário?
                    </h4>
                </b-col>
            </b-row>
        </b-modal>
    </div>
</template>

<script>
    // Método de requisição usando biblioteca Axios (importado de /src/utils/request.js)
    import request from '@/utils/request'
    // Método de alerta customizado (Biblioteca toastify-js) (importado de /src/utils/Alert.js)
    import Alert from '@/utils/Alert'


    export default {
        // Definindo propriedade para recarregar a lista de usuários após a exclusão
        props: ['refresh'],

        //Métodos usados nesse componente
        methods: {

            // Método usado para fazer a requisição de remoção do usuário
            removeUser(){
                request(
                    `api/user/${this.$store.state.current_user}/`,
                    'DELETE',
                    {},
                    (r)=>{
                        Alert(
                            'Usuário removido com sucesso',
                            's'
                        )
                        this.$emit('refresh')
                        this.$bvModal.hide('delete-user')
                    },
                    (error)=>{
                        Alert(
                            `Desculpe, não foi possível remover o usuário`,
                            's'
                        )
                    }
                )
            },
        }
    }
</script>