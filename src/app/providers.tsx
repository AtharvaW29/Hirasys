import { NextUIProvider } from '@nextui-org/system'

export type ProvidersProps = {
  children: React.ReactNode
}

const Providers = ({ children }: ProvidersProps) => {
  return <NextUIProvider>{children}</NextUIProvider>
}

export default Providers
