import { Input } from '@nextui-org/input'
import { MingcuteSearchLine, SolarBellLinear } from '../ui/icons'
import { Avatar } from '@nextui-org/avatar'

const Navigation = () => {
  return (
    <div className="h-[9vh] bg-overlay border-b-1 sticky top-0 flex items-center pl-12 pr-3">
      <Input
        startContent={<MingcuteSearchLine className="text-text-muted" />}
        placeholder="Search for Services"
        variant="bordered"
        className="w-[320px] text-text-muted"
      />
      <div className="ml-auto flex items-center gap-3">
        <SolarBellLinear className="w-9 h-9 text-text-muted" />
        <div className="border-l-1 px-4 flex items-center ">
          <Avatar />
          <p>Sakshi Upadhyay</p>
        </div>
      </div>
    </div>
  )
}

export default Navigation
